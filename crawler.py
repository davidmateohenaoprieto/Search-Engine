from utils.CustomRequests import CustomRequests as CR
from utils.URLVerification import URLVerification as Util

def go(n:int, dictionary:str, output:str):
    """La URL de inicio es : https://educacionvirtual.javeriana.edu.co/nuestros-programas-nuevo 
    el dominio limitante es: educacionvirtual.javeriana.edu.co"""

    url = "https://educacionvirtual.javeriana.edu.co/nuestros-programas-nuevo"
    domain = "educacionvirtual.javeriana.edu.co"

    # Ejemplo de uso funcion is absolute url
    url1 = "https://www.ejemplo.com"
    url2 = "/ruta/relativa"

    print(Util.is_absolute_url(url1))  # True
    print(Util.is_absolute_url(url2))  # False

    #Ejemplo de uso funcion convert_if_relative_url
    url_pagina_actual = "https://www.ejemplo.com/carpeta/pagina.html"
    url_relativa = "../imagen.jpg"

    url_absoluta = Util.convert_if_relative_url(url_pagina_actual, url_relativa)
    print(url_absoluta)

    # Ejemplo de uso funcion remove_fragment
    url_con_fragmento = "https://www.ejemplo.com/index.html#minorprogramincomputerscience"
    url_sin_fragmento = Util.remove_fragment(url_con_fragmento)
    print(url_sin_fragmento)

    #Verificaciones de metodos de CustomRequests
        # URL de ejemplo
    #url = "https://www.example.com"

    # Obtener la solicitud
    request = CR.get_request(url)
    if request:
        print("Solicitud exitosa.")
        # Si la solicitud fue exitosa, leer el contenido de la respuesta
        content = CR.read_request(request)
        print("Contenido de la respuesta:", content)

        # Obtener la URL asociada con la solicitud
        request_url = CR.get_request_url(request)
        print("URL de la solicitud:", request_url)
    else:
        print("La solicitud no fue exitosa.")    


def main():
    # Lógica principal de tu programa
    go(5, "Ingeniería de Software", "output.txt")

if __name__ == "__main__":
    main()
