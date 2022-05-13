from flask import render_template, session
import json
from routes.__init__ import routes
from models.Movies import Movie
from configuration import db
from routes.movies import *


@routes.route("/")
def home():
    user={'id':'','userName':'','email':'','password':'','dateCreated':''}
    if "user" in session:
        user=session["user"]
    return render_template("home/index.html", user=user)

@routes.route("/movie/<int:id>")
def infoMovie(id):
    return render_template("home/movie.html", movie=Movie.query.get(id).toJson())



@routes.route("/add/movies")
def moviess():
    movies=dict()
    with open('./movies.json', 'r') as f:
        moviesJSON=json.load(f)
        movies=moviesJSON['results']
    print(movies)
    for movie in movies:
        moviesDATA={
        "nombre": movie['original_title'],
        "imagenURL": f"https://www.themoviedb.org/t/p/original{movie['poster_path']}",
        "fechaEstreno": movie["release_date"],
        "description":movie['overview'],
        "dateCreated":"2022-05-05 09:24"
        }
        movie=Movie(data=moviesDATA)
        db.session.add(movie)
        db.session.commit()
    db.session.close()
    return 'aaa'
