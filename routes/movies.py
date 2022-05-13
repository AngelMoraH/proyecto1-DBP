from flask import jsonify, request
from configuration import db, sys
from models.Movies import Movie
#from routes.likes import getLikesById
from . import routes


@routes.route("/movies/")
def getMovies():
    res = Movie.query.all()
    """for i in range(0,len(res)):
        likes=getLikesById(res[i].id)
        res[i].data["likes"]=likes
    res= sorted(res, key=lambda x: x.data["likes"], reverse=True)"""
    return jsonify({"movies": [m.toJson() for m in res]})


@routes.route("/movies/<int:movieID>")
def getMoviesById(movieID):
    movie = Movie.query.filter_by(id=movieID).first()
    return jsonify({"movie": movie.toJson()})


@routes.route("/movies/", methods=["POST"])
def createMovie():
    response = {}
    message = ""
    try:
        request_data = request.get_json()
        movie = Movie(data=request_data["data"])
        db.session.add(movie)
        db.session.commit()
        response = movie.toJson()
        message = "Movie agregado con exito"
    except Exception as e:
        print(e)
        print(sys.exc_info())
        message = e
        db.session.rollback()
        pass
    finally:
        db.session.close()
    return jsonify({"message": message, "response": response})

@routes.route("/movies/<int:movieID>", methods=["PUT"])
def updateMovie(movieID):
    message=""
    try:
        movie=Movie.query.filter_by(id=movieID).first()
        nMovie = Movie.query.filter_by(id=movieID).update(dict(data=movie.data))
        db.session.commit()
        message='like de Movie actualizado con exito'
    except Exception as e:
        print(e)
        print(sys.exc_info())
        message=e
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({"message":message})

@routes.route("/movies/<int:movieID>", methods=["DELETE"])
def deleteMovie(movieID):
    message = ""
    try:
        movie = Movie.query.filter_by(id=movieID).first()
        db.session.delete(movie)
        db.session.commit()
        message = "pelicula eliminada con exito"
    except Exception as e:
        print(e)
        print(sys.exc_info())
        message = e
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({"message": message})
