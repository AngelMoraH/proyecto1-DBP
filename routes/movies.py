import http
from flask import jsonify, request,abort
from configuration import db
from models.Movies import Movie
from . import routes


@routes.route("/movies/")
def getMovies():
    res = Movie.query.all()
    return jsonify({"movies": [m.toJson() for m in res]})



@routes.route("/movies/<int:movieID>")
def getMoviesById(movieID):
    status_code=0
    movie = Movie.query.filter_by(id=movieID).first()
    if movie !=None:
        status_code =http.HTTPStatus.ACCEPTED
        return jsonify({"movie": movie.toJson(),"status_code":status_code})
    else:
        status_code =http.HTTPStatus.INTERNAL_SERVER_ERROR
        abort(status_code)
    


@routes.route("/movies/", methods=["POST"])
def createMovie():
    response = {}
    message = ""
    status_code=0
    try:
        request_data = request.get_json()
        movie = Movie(data=request_data['data'])
        db.session.add(movie)
        db.session.commit()
        response = movie.toJson()
        message = "Movie agregado con exito"
        status_code =http.HTTPStatus.ACCEPTED
    except Exception as e:
        db.session.rollback()
        abort(status_code)
    finally:
        db.session.close()
    return jsonify({"message": message, "response": response, "status_code": status_code})

@routes.route("/movies/<int:movieID>", methods=["PUT"])
def updateMovie(movieID):
    message=""
    status_code=0
    try:
        movie=Movie.query.filter_by(id=movieID).first()
        movieDATA = request.get_json()['data']
        nMovie = Movie.query.filter_by(id=movieID).update(dict(data=movieDATA))
        db.session.commit()
        message='Movie actualizado con exito'
        status_code =http.HTTPStatus.ACCEPTED
    except Exception as e:
        db.session.rollback()
        status_code =http.HTTPStatus.INTERNAL_SERVER_ERROR
        abort(status_code)
    finally:
        db.session.close()
    return jsonify({"message":message, "status_code":status_code})

@routes.route("/movies/<int:movieID>", methods=["DELETE"])
def deleteMovie(movieID):
    message = ""
    status_code=0
    try:
        movie = Movie.query.filter_by(id=movieID).first()
        db.session.delete(movie)
        db.session.commit()
        message = "pelicula eliminada con exito"
        status_code =http.HTTPStatus.ACCEPTED
    except Exception as e:
        db.session.rollback()
        abort(status_code)
    finally:
        db.session.close()
    return jsonify({"message": message, "status_code": status_code})
