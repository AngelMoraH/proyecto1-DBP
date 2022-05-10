
# HORRORPEDIA

<img style="width: 150px;" src='static/imgs/grm.png' alt='logo'/>

<center>

<h2>INTEGRANTES:</h2>
<div>
  <table style="width: 100%; display: flex; justify-content:center;">
    <tr>
      <th>Nombre y Apellido</th>
      <th>Código</th>
      <th>Roles</th>
    </tr>
    <tr>
      <th>Angel Mora Huamanchay</th>
      <th>202010031</th>
      <th>Backend</th>
    </tr>
    <tr>
      <th>Angel Gabriel Mucha Huaman</th>
      <th>202110701</th>
      <th>Frontend</th>
    </tr>
    <tr>
      <th>Johan Fabian Callinapa Chunga</th>
      <th>202110706</th>
      <th>Frontend</th>
    </tr>
  </table>
</div>
</center>
<hr/>

## DESCRIPCIÓN DEL PROYECTO

Nuestro proyecto es una página web que contiene una lista de películas de terror con su respectiva información:
* **Título de la película**
* **Poster de la película**
* **Fecha de estreno de la película**
* **Descripción de la película**

Donde los usuarios van a poder ver los comentarios realizados por otros usuarios sobre aquellas películas y también podrán comentar sobre ellas, pero no solo eso, también podrán dar una calificación a la película y un me gusta al comentario.

Para mostrar los comentarios tendremos en cuenta la cantidad de me gusta de cada uno para así ordenarlo de forma descendente mostrando los comentarios que poseen una mayor cantidad de me gusta al comienzo. 

Solamente los usuarios registrados pueden comentar, dar me gusta y calificar las películas por lo cuál hemos implementado una autenticación usando varias función provenientes de ***FLASK*** para poder manejar la sesión de un usuario, y también para poder encriptar la contraseña del usuario al momento que se registrar y poder validarla al momento que inicia sesión. 
<hr/>

## MISIÓN
Nuestra misión es proveer a nuestros usuarios, amantes de las películas de terror, un espacio donde puedan encontrar películas tanto recién estrenadas o antiguas con su respectiva información, así como también los comentarios y opiniones acerca de ellas para así facilitarle la elección de alguna película para su noche de cine. 
## VISIÓN
Nuestra visión es convertirnos en una de las mejores páginas web de películas de terror en el Perú y también en Latinoamérica.
<hr/>

## LIBRERÍAS UTILIZADAS
Las librerías utilizadas en el proyecto son:
* **Flask:** Es un “micro” Framework escrito en Python y concebido para facilitar el desarrollo de Aplicaciones Web.
* **SQLAlchemy:** Es el kit de herramientas SQL de Python y Object Relational Mapper que brinda a los desarrolladores de aplicaciones toda la potencia y flexibilidad de SQL.
* **psycopg2:** Es el adaptador de base de datos PostgreSQL más popular para el lenguaje de programación Python.
* **python-dotenv:** Lee pares clave-valor de un archivo y puede establecerlos como variables de entorno.
* **Werkzeug:** Es una completa biblioteca de aplicaciones web WSGI. Comenzó como una simple colección de varias utilidades para aplicaciones WSGI y se ha convertido en una de las bibliotecas de utilidades WSGI más avanzadas.
* **Flask-Migrate:** Es una extensión que maneja las migraciones de bases de datos SQLAlchemy para aplicaciones Flask que usan Alembic.
<hr/>

# Información acerca de los endpoint
* En el archivo home.py se encuentran los siguientes los endpoints: 
  * **home:** Es la encargada de renderizar la página principal de nuestro proyecto y de validar si el usuario esta logeado.
  * **infoMovie:** Es la encargada de realizar la lógica para obtener la información de la pelicula seleccionada y renderizar la página con aquella información.
* En el archivo users.py se encuentran los siguientes los endpoints:
  * **login:** Este endpoint es el encargado de renderizar la página de inicio de sesión y de realizar la lógica de validación del email y la contraseña. Si la validación es exitosa se agrega a la sesión de la aplicación la información del usuario logueado, de lo contrario se envía los mensajes correspondientes de error.
  * **register:** Este endpoint es el encargado de renderizar la página de registro de usuario y de realizar la validación del username, email y contraseña para que el usuario pueda registrarse de manera exitosa en la página web.
  * **logout:** Este endpoint es el encargado de realizar la lógica de cierre de sesión del usuario en la página web.

* En el archivo movies.py se encuentran los siguientes los endpoints:
  * **getMovies:** Es el encargado de obtener la lista de películas de terror de la base de datos y tambien de agregarle la calificación de la película.
  * **getMoviesById:** Es el encargado de obtener y mandar toda la información de la película seleccionada, através de su id, al cliente.
  * **createMovie:** Este endpoint es el encargado de crear y agregar una película en la base de datos.
  * **updateMovie:** Este endpoint es el encargado de actualizar la información, especialmente la calificación de la película en la base de datos.
  * **deleteMovie:** Este endpoint es el encargado de eliminar una película através de su id en la base de datos.
* En el archivo comentario.py se encuentran los siguientes los endpoints:
  * **getComentarios:** Este endpoint es el encargado de obtener la lista de comentarios de la base de datos, agregarle la cantidad de likes que posee y ordenarla de forma descendente por la cantidad de likes.
  * **createComentario:** Este endpoint es el encargado de crear y agregar un comentario realizado por el usuario en la base de datos.
  * **updateComentario:** Este endpoint es el encargado de actualizar la información de un comentario, especialmente la cantidad de likes en la base de datos.
  * **deleteComentario:** Este endpoint es el encargado de eliminar un comentario através de su id en la base de datos.
<hr/>

# Hosts
* El **proyecto** se encuentra en **localhost:5000**

* Nuestra **base de datos** se encuentra en **ec2-54-164-40-66.compute-1.amazonaws.com**. El motivo por el cuál subimos nuestra base de datos a un host remoto es por la facilidad al momento de diseñar el front-end de nuestra página web, ya que si hubiesemos dejado nuestra base de datos en el local al momento que un integrante desee ver los datos tendría que agregarlos el mismo a su base de datos local, obviamente este proceso no es el adecuado por lo cuál como grupo tomamos la decisión de subir nuestra base de datos a un host remoto proveido por **Heroku**.
<hr/>