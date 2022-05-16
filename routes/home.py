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


