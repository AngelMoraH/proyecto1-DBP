import http
import json
from flask import jsonify, render_template, request,abort
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
