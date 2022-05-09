# HORRORPEDIA
* **INTEGRANTES**:
  | nombre y apellido | código |
  |-------------------|--------|
  | Angel Mora Huamanchay | 202010031 |
  | Angel Gabriel Mucha Huaman | 202110701 |
  | Johan Fabian Callinapa Chunga| 202110706 |

## DESCRIPCIÓN DEL PROYECTO
Nuestro proyecto es una página web que contiene una lista de películas de terror con su respectiva información:
* **Título de la película**
* **Poster de la película**
* **Fecha de estreno de la película**
* **Descripción de la película**

Donde los usuarios van a poder ver los comentarios realizados por otros usuarios sobre aquellas películas y también podrán comentar sobre ellas, pero no solo eso, también podrán dar una calificación a la película y un me gusta al comentario.

Para mostrar los comentarios tendremos en cuenta la cantidad de me gusta de cada uno para así ordenarlo de forma descendente mostrando los comentarios que poseen una mayor cantidad de me gusta al comienzo. 

Solamente los usuarios registrados pueden comentar, dar me gusta y calificar las películas por lo cuál hemos implementado una autenticación usando varias función provenientes de ***FLASK*** para poder manejar la sesión de un usuario, y también para poder encriptar la contraseña del usuario al momento que se registrar y poder validarla al momento que inicia sesión. 

## MISIÓN
Nuestra misión es proveer a nuestros usuarios, amantes de las películas de terror, un espacio donde puedan encontrar películas tanto recién estrenadas o antiguas con su respectiva información, así como también los comentarios y opiniones acerca de ellas para así facilitarle la elección de alguna película para su noche de cine. 
## VISIÓN
Nuestra visión es convertirnos en una de las mejores páginas web de películas de terror en el Perú y también en Latinoamérica.

## LIBRERÍAS UTILIZADAS
Las librerías utilizadas en el proyecto son:
* **Flask:** Es un “micro” Framework escrito en Python y concebido para facilitar el desarrollo de Aplicaciones Web.
* **SQLAlchemy:** Es el kit de herramientas SQL de Python y Object Relational Mapper que brinda a los desarrolladores de aplicaciones toda la potencia y flexibilidad de SQL.
* **psycopg2:** Es el adaptador de base de datos PostgreSQL más popular para el lenguaje de programación Python.
* **python-dotenv:** Lee pares clave-valor de un archivo y puede establecerlos como variables de entorno.
* **Werkzeug:** Es una completa biblioteca de aplicaciones web WSGI. Comenzó como una simple colección de varias utilidades para aplicaciones WSGI y se ha convertido en una de las bibliotecas de utilidades WSGI más avanzadas.

# Hosts
* El **proyecto** se encuentra en **localhost:5000**

* Nuestra **base de datos** se encuentra en **ec2-54-164-40-66.compute-1.amazonaws.com**. El motivo por el cuál subimos nuestra base de datos a un host remoto es por la facilidad al momento de diseñar el front-end de nuestra página web, ya que si hubiesemos dejado nuestra base de datos en el local al momento que un integrante desee ver los datos tendría que agregarlos el mismo a su base de datos local, obviamente este proceso no es el adecuado ya que si tuviesemos varios modelos y datos realizar esta acción no es eficiente por lo cuál como grupo tomamos la decisión de subir nuestra base de datos a un host remoto proveido por **Heroku**.