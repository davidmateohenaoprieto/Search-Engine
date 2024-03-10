# Laboratorio 2 - Analitica de Datos 
##### En este laboratorio, desarrollarás un motor de búsqueda de cursos y un rastreador web que recopila información de un catálogo universitario para construir un índice. El objetivo es brindarte experiencia en programación en Python y trabajar con documentos HTML obtenidos de la web.
#### Autores: Gabriela Mercedes Luigi, David Mateo Henao

- ##### Introducción:
  Para el desarrollo de este taller vamos a estar utilizando como nuestra  base de información el portal Web de la Javeriana para los cursos que la universidad ofrece parte de las carreras de Pregrado, Posgrados y Titulaciones. Este fue el enlace utilizado para el desarrollo de este proyecto: 
  https://educacionvirtual.javeriana.edu.co/temporomandibulares

  Con el fin de lograr este objetivo, desarrollaron tres programas principales: crawler.py, search.py y compare.py, cada uno desempeñando un papel crucial en el proceso de recopilación, búsqueda y comparación de datos.

- ##### Procedimiento:

  En primer lugar, el programa crawler.py se encargó de rastrear el sitio web de la universidad objetivo y extraer información relevante sobre los cursos         disponibles. Utilizando la biblioteca BeautifulSoup para analizar el contenido HTML de las páginas web, el rastreador identificó los elementos que contenían detalles sobre los cursos, tales como el nombre, la duración, el nivel de dificultad, la fecha de inicio y el precio. Luego de recolectar estos datos, los almacenó en un formato estructurado, primero en un archivo JSON para una fácil manipulación y luego exportándolos a un archivo CSV para un análisis más tabular y accesible.

  Con la información recopilada y almacenada, el siguiente paso fue facilitar a los usuarios la búsqueda de cursos relevantes. Para ello, se implementó el programa search.py, que permitió a los usuarios especificar sus intereses mediante una lista de palabras clave. El programa cargó los datos de los cursos desde el archivo JSON generado previamente y realizó una búsqueda exhaustiva, buscando coincidencias entre los intereses proporcionados y los nombres de los cursos. Esto resultó en una lista de cursos que coincidían con los intereses del usuario, lo que simplificó significativamente el proceso de búsqueda y selección de cursos relevantes.

  Finalmente, para brindar una funcionalidad adicional de comparación entre cursos, se desarrolló el programa compare.py. Este programa evaluó la similitud entre dos cursos dados, considerando diferentes atributos como la duración, el nivel de dificultad, la fecha de inicio y el precio. Asignando pesos a cada atributo para reflejar su importancia relativa en la comparación, el programa calculó una puntuación de similitud total, lo que permitió a los usuarios tomar decisiones informadas al elegir entre cursos similares.


- ##### Analisis de Datos:
  
  el archivo cursos.json sirve como un repositorio estructurado de datos que almacena información detallada sobre los cursos ofrecidos por la universidad. Cada entrada en este archivo representa un curso específico y contiene los siguientes atributos:

    - id: Un identificador único para el curso, que facilita la referencia y la identificación dentro del conjunto de datos.
    - nombre: El nombre completo del curso, proporcionando una descripción clara y concisa del contenido y el enfoque del curso.
    - enlace: Un enlace URL que dirige al usuario a la página web oficial del curso, lo que facilita el acceso directo a información adicional, detalles de inscripción         y otros recursos relacionados con el curso.
    - duracion: La duración estimada del curso, expresada en horas, proporcionando una indicación del compromiso de tiempo requerido para completar el curso.
    - nivel: El nivel de dificultad del curso, que puede variar desde básico hasta avanzado, lo que permite a los estudiantes seleccionar cursos que se alineen con su nivel de habilidad y experiencia.
    - fecha_inicio: La fecha de inicio del curso o una indicación de que comenzará próximamente, lo que permite a los estudiantes planificar su participación en el curso de acuerdo con su disponibilidad y horario.
    - precio: El costo del curso, expresado en la moneda local, proporcionando información crucial para los estudiantes sobre los aspectos financieros asociados con la participación en el curso.

- ##### Conclusiones:
  
  - Facilitación del acceso a la información: Los motores de búsqueda y los rastreadores web son herramientas fundamentales para facilitar el acceso a la información en la era digital. Permiten a los usuarios buscar y acceder a contenido relevante de manera rápida y eficiente, lo que resulta esencial en un mundo donde la cantidad de información disponible es abrumadora.
  - Automatización de tareas de recolección de datos: Los rastreadores web, como el implementado en el laboratorio, automatizan el proceso de recolección de datos al recorrer páginas web y extraer información específica. Esto ahorra tiempo y esfuerzo, especialmente cuando se trata de recopilar grandes cantidades de datos de múltiples fuentes en línea.
  - Análisis y comparación de datos: Los datos recopilados por los rastreadores web pueden ser analizados y comparados utilizando herramientas como el motor de búsqueda y el comparador implementados en el laboratorio. Estas herramientas permiten a los usuarios encontrar información relevante y tomar decisiones informadas basadas en la comparación de diferentes cursos u otros conjuntos de datos.
  - Personalización y adaptabilidad: Los motores de búsqueda y rastreadores web en Python pueden ser adaptados y personalizados para satisfacer necesidades específicas. En el laboratorio, se desarrollaron programas que se ajustaban a los requisitos del proyecto, pero estas herramientas pueden ser modificadas para adaptarse a una variedad de aplicaciones y contextos diferentes.
  - Conclusión final: el laboratorio destacó la importancia y el valor de las herramientas como motores de búsqueda y rastreadores web en Python en el contexto actual, donde el acceso a la información es crucial y la automatización de tareas de recolección y análisis de datos es cada vez más necesaria. Estas herramientas no solo simplifican el proceso de búsqueda y análisis de información, sino que también permiten a los usuarios tomar decisiones más informadas y eficientes en una amplia gama de aplicaciones y disciplinas.
