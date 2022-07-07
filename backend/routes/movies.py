import http
import json
from flask import jsonify, request, abort
from configuration import db
from models.Movies import Movie
from . import routes

CANT_MOVIES = 10


def paginate_movies(request, selection, isDesc=False):
    if isDesc:
        start = len(selection) - CANT_MOVIES
        end = len(selection)
    else:
        page = request.args.get("page", 1, type=int)
        start = (page - 1) * CANT_MOVIES
        end = start + CANT_MOVIES
    movies = [movie.toJson() for movie in selection]
    current_movies = movies[start:end]
    return current_movies


@routes.route("/movies", methods=["GET"])
def getMovies():
    error_404=False
    try:
        exist=False
        search=request.args.get('search', "", type=str)
        if search != "":
            movies=Movie.query.all()
            search_movies=[]
            for m in movies:
                if search.lower() in m.data['nombre'].lower():
                    exist=True
                    search_movies.append(m)
            if exist:
                moviesSearch = paginate_movies(request, search_movies, False)
                print(moviesSearch)
                return jsonify({
                    'success': True,
                    'movies': moviesSearch,
                    'total_movies': len(search_movies)
                })
            else:
                error_404=True
                abort(404)
        selection = Movie.query.order_by("id").all()
        movies = paginate_movies(request, selection)

        if len(movies) == 0:
            abort(404)

        return jsonify({"success": True, "movies": movies, "total_movies": len(selection)})
    except:
        db.session.rollback()
        if error_404:
            abort(404)
        else:
            abort(500)
        pass


@routes.route("/movies/<int:movieID>")
def getMoviesById(movieID):
    status_code = 0
    error_404 = False
    try:
        movie = Movie.query.filter_by(id=movieID).one_or_none()
        if movie is None:
            error_404 = True
            abort(404)

        status_code = http.HTTPStatus.ACCEPTED
        return jsonify(
            {"movie": movie.toJson(), "status_code": status_code, "success": True}
        )
    except:
        db.session.rollback()
        if error_404:
            abort(404)
        else:
            abort(500)


@routes.route("/movies", methods=["POST"])
def createMovie():
    response = {}
    message = ""
    status_code = 0
    error_422 = False
    try:
        body = request.get_json()

        data = body.get("data", None)
        if data is None:
            error_422 = True
            abort(422)

        movie = Movie(data=data)
        db.session.add(movie)
        db.session.commit()
        response["movie"] = movie.toJson()
        response["success"] = True
        message = "pelicula agregada con exito"
        status_code = http.HTTPStatus.ACCEPTED
        return jsonify(
            {
                "message": message,
                "movie": response["movie"],
                "status_code": status_code,
                "success": response["success"],
            }
        )

    except Exception as e:
        db.session.rollback()
        if error_422:
            abort(422)
        else:
            abort(500)

    finally:
        db.session.close()


@routes.route("/movies/<int:movieID>", methods=["PUT"])
def updateMovie(movieID):
    message = ""
    status_code = 0
    error_404 = False
    error_422 = False
    try:
        movie = Movie.query.filter_by(id=movieID).one_or_none()
        if movie is None:
            error_404 = True
            abort(404)

        body = request.get_json()
        movieDATA = body.get("data", None)
        if movieDATA is None:
            error_422 = True
            abort(422)

        nMovie = Movie.query.filter_by(id=movieID).update(dict(data=movieDATA))
        db.session.commit()
        message = "pelicula actualizada con exito"
        status_code = http.HTTPStatus.ACCEPTED

        return jsonify(
            {
                "message": message,
                "status_code": status_code,
                "success": True,
                "movie_id": movieID,
            }
        )
    except Exception as e:
        db.session.rollback()
        if error_404:
            abort(404)
        elif error_422:
            abort(422)
        else:
            abort(500)
    finally:
        db.session.close()


@routes.route("/movies/<int:movieID>", methods=["DELETE"])
def deleteMovie(movieID):
    message = ""
    status_code = 0
    error_404 = False
    try:
        movie = Movie.query.filter_by(id=movieID).one_or_none()
        if movie is None:
            error_404 = True
            abort(404)

        db.session.delete(movie)
        db.session.commit()
        selection = Movie.query.order_by("id").all()
        movies = paginate_movies(request, selection, True)
        message = "pelicula eliminada con exito"
        status_code = http.HTTPStatus.ACCEPTED
        return jsonify({
            "message": message, 
            "status_code": status_code,
            'success': True,
            'delete_movie': movieID,
            'movies': movies,
            'total_movies': len(selection)
        })
    except Exception as e:
        db.session.rollback()
        if error_404:
            abort(404)
        else:
            abort(500)
    finally:
        db.session.close()
