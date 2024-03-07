import requests
from selenium import webdriver


class CustomRequests:
    
    def get_request(url):
        try:
            # Realizar la solicitud HTTP GET y devolver el objeto Response
            response = requests.get(url)
            # Verificar el estado de la respuesta
            if response.status_code == 200:
                return response
            else:
                # Devolver None si la solicitud no fue exitosa
                return None
        except requests.exceptions.RequestException:
            # Devolver None si ocurre algún error durante la solicitud
            return None

    def read_request(request):
        driver = webdriver.Chrome()
        driver.get(request.url)
        html_content = driver.page_source
        return html_content

    def get_request_url(request):
        # Obtener la URL asociada con la solicitud
        return request.url