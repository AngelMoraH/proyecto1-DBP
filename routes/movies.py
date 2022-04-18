from flask import Response,request
from configuration import db
from models.Movies import Movie
from . import routes


@routes.route("/movies/")
def getMovies():
    res = Movie.query.all()
    movies={}
    movies["movies"]=[]
    for movie in res:
        movies["movies"].append(movie.toJson())
    return Response(response=str(movies["movies"]),)


@routes.route("/movies/<int:movieID>")
def getMoviesById(movieID):
    movie = Movie.query.filter_by(id=movieID).first()
    print(movie)
    return Response(str(movie.toJson()))


@routes.route("/movies/", methods=["POST"])
def createMovie():
    request_data = request.get_json()
    movie = Movie(
        nombre=request_data["nombre"],
        imagenURL=request_data["imagenURL"],
        añoEstreno=request_data["añoEstreno"],
        director=request_data["director"],
        dateCreated=request_data["dateCreated"],
    )
    db.session.add(movie)
    db.session.commit()
    db.session.close()
    return "pelicula agregada con exito"

@routes.route("/movies/<int:movieID>",methods=["DELETE"])
def deleteMovie(movieID):
    movie = Movie.query.filter_by(id=movieID).first()
    db.session.delete(movie)
    db.session.commit()
    db.session.close()
    return "pelicula eliminada con exito"
