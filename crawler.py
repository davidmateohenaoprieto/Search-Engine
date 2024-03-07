from utils.CustomRequests import CustomRequests as CR
from utils.URLVerification import URLVerification as Util
from utils.CoursesDict import CoursesDict as CD
import bs4
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

def go(n:int, dictionary:str, output:str):
    return 0



def main():
    """Funcion que se encarga de realizar el web scraping de la pagina de la universidad 
    Javeriana para la lista de cursos que ofrece en su portal web y crear un archivo con dicha información
    (Se comenta la función ya que el archivo ya está creado)
    """
    #coursesWebScraping("https://educacionvirtual.javeriana.edu.co/nuestros-programas-nuevo")

    """
    Función que se va a encargar de crear el índice de mapea palabras a cursos
    """
    n=input("Ingrese el número de páginas a rastrear: ")
    dictionary="cursos.json"
    output=input("Ingrese el nombre del archivo de salida: ")
    output+=".txt"
    go(n,dictionary,output)

if __name__ == "__main__":
    main()
