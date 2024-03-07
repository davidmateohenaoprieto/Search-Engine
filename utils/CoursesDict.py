import bs4
import json

class CoursesDict:

    @staticmethod
    def listCourses(htmlContent):
        cursos_list = []
        url_base = "https://educacionvirtual.javeriana.edu.co"
        
        soup = bs4.BeautifulSoup(htmlContent, 'html5lib')
        
        curso_elements = soup.find_all('li', class_='item-programa')
        curso_elements_filtered = [element for element in curso_elements if element.find('div', class_='card-type course font-weight-bold text-white') and "Curso" in element.find('div', class_='card-type course font-weight-bold text-white').text]

        for i, curso in enumerate(curso_elements_filtered, 1):
            nombre = curso.find('b', class_='card-title').text.strip()
            enlace = curso.find('a')['href']
            
            if enlace.startswith("/"):
                enlace_completo = url_base + enlace
            else:
                enlace_completo = enlace

            print(nombre)
            print(enlace_completo)
            
            duracion, nivel, fecha_inicio, precio = "", "", "", ""
            
            small_tags = curso.find_all('small')
            for small in small_tags:
                text = small.text.strip()
                if ":" in text:
                    title, content = text.split(":", 1)
                    content = content.strip()
                    if title == "Duración":
                        duracion = content
                    elif title == "Nivel":
                        nivel = content
                    elif title == "Fecha de inicio":
                        fecha_inicio = content
                    elif title == "Precio":
                        precio = content
                else:
                    print(text)
                print("------------")

            curso_data = {
                "id": i,
                "nombre": nombre,
                "enlace": enlace_completo,
                "duracion": duracion,
                "nivel": nivel,
                "fecha_inicio": fecha_inicio,
                "precio": precio
            }
            
            cursos_list.append(curso_data)
            
        return cursos_list
        
    @staticmethod
    def generarJSON(cursos):
        with open('cursos.json', 'w', encoding='utf-8') as json_file:
            json.dump(cursos, json_file, indent=4, ensure_ascii=False)

        print("Los cursos han sido guardados en el archivo 'cursos.json'.")

