from utils.CustomRequests import CustomRequests as CR
from utils.URLVerification import URLVerification as Util
from utils.CoursesDict import CoursesDict as CD
from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse
from queue import Queue
import json
import csv

def coursesWebScraping(url:str):
    # Obtener la solicitud
    request = CR.get_request(url)
    if request:
        print("Solicitud exitosa.")
        # Si la solicitud fue exitosa, leer el contenido de la respuesta
        content = CR.read_request(request)
        # Obtener la URL asociada con la solicitud
        request_url = CR.get_request_url(request)
        print("URL de la solicitud:", request_url)
    else:
        print("La solicitud no fue exitosa.")

    cursos=CD.listCourses(content)
    CD.generarJSON(cursos)

class CourseCrawler:
    def __init__(self, start_url, domain):
        self.start_url = start_url
        self.domain = domain
        self.visited_urls = set()

    @staticmethod
    def is_url_ok_to_follow(url, domain):
        """
        Verifica si una URL es aceptable para seguir basada en ciertos criterios.
        """
        if not url.startswith("http"):
            return False
        if "@" in url or "mailto:" in url:
            return False
        if not url.endswith((".html", "/")):
            return False
        if domain not in url:
            return False
        return True

    def get_request(self, url):
        return requests.get(url)

    def find_links(self, url):
        response = self.get_request(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [link.get('href') for link in soup.find_all('a', href=True)]
            return links
        return []

    def crawl(self, n):
        queue = Queue()
        queue.put(self.start_url)
        visited_count = 0

        while not queue.empty() and visited_count < n:
            url = queue.get()
            if url not in self.visited_urls:
                if self.is_url_ok_to_follow(url, self.domain):
                    links = self.find_links(url)
                    for link in links:
                        if link not in self.visited_urls:
                            queue.put(link)
                    self.visited_urls.add(url)
                    visited_count += 1

class Indexer:
    def __init__(self, dictionary_file):
        self.dictionary_file = dictionary_file
        self.index = {}
        self.load_stop_words("stop_words.json")  # Cargar palabras irrelevantes

    def index_course(self, course_id, title, description):
        # Convertir a minúsculas y eliminar caracteres no deseados al final
        title = re.sub(r'[^\w\s]', '', title.lower())
        description = re.sub(r'[^\w\s]', '', description.lower())

        # Dividir en palabras y filtrar palabras comunes
        words = [word for word in title.split() + description.split() if len(word) > 1 and word not in self.stop_words]

        # Indexar las palabras
        for word in words:
            self.index.setdefault(word, set()).add(course_id)

    def load_stop_words(self, stop_words_file):
        with open(stop_words_file, 'r') as f:
            self.stop_words = set(json.load(f))

    def index_courses_from_json(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            courses = json.load(f)
            for course in courses:
                self.index_course(str(course['id']), course['nombre'], "")


    def save_index_to_csv(self, output_file):
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
            for word, course_ids in self.index.items():
                for course_id in course_ids:
                    writer.writerow([course_id, word])



class CourseComparator:
    def __init__(self, index):
        self.index = index

    def compare(self, course1_id, course2_id):
        course1_words = set(self.index.get(course1_id, []))
        course2_words = set(self.index.get(course2_id, []))
        common_words = course1_words.intersection(course2_words)
        
        # Verificar si hay palabras comunes
        if not common_words:
            return 0.0
        
        # Calcular la similitud evitando la división por cero
        similarity = len(common_words) / (len(course1_words) + len(course2_words) - len(common_words))
        return similarity


class CourseSearcher:
    def __init__(self, index):
        self.index = index

    def search(self, keywords):
        relevant_courses = {}
        for keyword in keywords:
            for course_id in self.index.get(keyword.lower(), []):
                relevant_courses[course_id] = relevant_courses.get(course_id, 0) + 1
        sorted_courses = sorted(relevant_courses.items(), key=lambda x: x[1], reverse=True)
        return [course_id for course_id, relevance in sorted_courses]


def find_non_zero_similarity(comparator, courses):
    for course1_id in courses:
        for course2_id in courses:
            if course1_id != course2_id:
                similarity = comparator.compare(course1_id, course2_id)
                if similarity != 0.0:
                    return course1_id, course2_id, similarity
    return None, None, None

def go(n:int, dictionary:str, output:str):
    crawler = CourseCrawler("https://educacionvirtual.javeriana.edu.co/nuestros-programas-nuevo", "educacionvirtual.javeriana.edu.co")
    crawler.crawl(n)

    indexer = Indexer(dictionary)
    indexer.load_stop_words("stop_words.json")
    indexer.index_courses_from_json("cursos.json")
    indexer.save_index_to_csv(output)

    # Después de haber construido el índice de cursos
    comparator = CourseComparator(indexer.index)
    searcher = CourseSearcher(indexer.index)

    # Suponiendo que courses es una lista de todos los identificadores de cursos
    courses = indexer.index.keys()

    # Usar el comparador de cursos para encontrar una similitud diferente de cero
    course1_id, course2_id, similarity = find_non_zero_similarity(comparator, courses)
    if similarity is not None:
        print("Se encontró una similitud diferente de cero entre los cursos:")
        print("Curso 1:", course1_id)
        print("Curso 2:", course2_id)
        print("Similitud:", similarity)
    else:
        print("No se encontró ninguna similitud diferente de cero entre los cursos.")

    # Ejemplo de uso del buscador
    keywords = ["fotografía", "luminosidad", "enfoque", "composición"]
    relevant_courses = searcher.search(keywords)
    print("Cursos relevantes encontrados con las palabras de prueba (fotografía, luminosidad, enfoque, composición):", relevant_courses)


def main():
    """Funcion que se encarga de realizar el web scraping de la pagina de la universidad 
    Javeriana para la lista de cursos que ofrece en su portal web y crear un archivo con dicha información
    (Se comenta la función ya que el archivo ya está creado)
    """
    #coursesWebScraping("https://educacionvirtual.javeriana.edu.co/nuestros-programas-nuevo")

    """
    Función que se va a encargar de crear el índice de mapea palabras a cursos
    """
    n=int(input("Ingrese el número de páginas a rastrear: "))
    dictionary="cursos.json"
    output=input("Ingrese el nombre del archivo de salida: ")
    output+=".csv"
    go(n,dictionary,output)

if __name__ == "__main__":
    main()
