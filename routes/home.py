from flask import redirect, render_template, session
import json
from models import comentario
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

@routes.route("/movie/<int:idMovie>/")
def infoMovie(idMovie):
    user={'id':'','userName':'','email':'','password':'','dateCreated':''}
    if "user" in session:
        user=session["user"]
    return render_template("home/movie.html", movie=Movie.query.get(idMovie).toJson(),idUser=user['id'],user=user)



@routes.route("/add/movies")
def agregarmoviesJSON():
    movies=dict()
    message=""
    try:
        with open('./movies.json', 'r') as f:
            moviesJSON=json.load(f)
            movies=moviesJSON['results']
            
        for movie in movies:
            moviesDATA={
            "nombre": movie['original_title'],
            "imagenURL": f"https://www.themoviedb.org/t/p/original{movie['poster_path']}",
            "fechaEstreno": movie["release_date"],
            "description":movie['overview'],
            "calificacion":movie['vote_average'],
            "dateCreated":"2022-05-05 09:24"
            }
            movie=Movie(data=moviesDATA)
            db.session.add(movie)
            db.session.commit()
        message="Movies agregados con exito"

    except Exception as e:
        message=e
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({"message":message})
