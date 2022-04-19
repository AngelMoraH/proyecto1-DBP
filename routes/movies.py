from flask import Response,request
from configuration import db
from models.Movies import Movie
from . import routes


@routes.route("/movies/")
def getMovies():
    res = Movie.query.all()
    return Response(str(res))


@routes.route("/movies/<int:movieID>")
def getMoviesById(movieID):
    movie = Movie.query.filter_by(id=movieID).first()

    return Response(str(movie))


@routes.route("/movies/", methods=["POST"])
def createMovie():
    request_data = request.get_json()
    movie = Movie(
        data=request_data["data"]
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
