# Import de la biblioteca estándar urllib.parse
import urllib.parse

class URLVerification:

    def remove_fragment(url):
        # Parsear la URL y obtener la URL base y el fragmento
        base_url, fragment = urllib.parse.urldefrag(url)
        return base_url

    def convert_if_relative_url(url1, url2):
        try:
            # Parsear la URL base (url1) y combinarla con la URL relativa (url2)
            absolute_url = urllib.parse.urljoin(url1, url2)
            return absolute_url
        except ValueError:
            # Si ocurre un error al parsear la URL, devolver None
            return None

    def is_absolute_url(url):
        parsed_url = urllib.parse.urlparse(url)
        return bool(parsed_url.scheme) and bool(parsed_url.netloc)
