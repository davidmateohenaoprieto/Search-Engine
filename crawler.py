import requests as req


def go(n:int, dictionary:str, output:str):
    """La URL de inicio es : https://educacionvirtual.javeriana.edu.co/nuestros-programas-nuevo 
    el dominio limitante es: educacionvirtual.javeriana.edu.co"""

    url = "https://educacionvirtual.javeriana.edu.co/nuestros-programas-nuevo"
    domain = "educacionvirtual.javeriana.edu.co"


    for i in range(n):
        print(f"El programa {dictionary} ha recorrido {i} páginas")
    return 0


def main():
    # Lógica principal de tu programa
    go(5, "Ingeniería de Software", "output.txt")

if __name__ == "__main__":
    main()
