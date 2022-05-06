from flask import jsonify, request
from configuration import db, sys
from models.calificacion import Calificacion
from . import routes


@routes.route("/likes/")
def getCalificaciones():
    res = Calificacion.query.all()
    return jsonify({"calificacion": [l.toJson() for l in res]})


@routes.route("/likes/<int:movieID>/")
def getCalificacionById(movieID):
    try:
        res = Calificacion.query.all()
        totalCalificacion = 0
        for calificacion in res:
            if calificacion.data["iMmovie"] == movieID:
                totalCalificacion += 1
    except Exception as e:
        print(e)
        print(sys.exc_info())

    return totalCalificacion 


@routes.route("/likes/", methods=["POST"])
def addLike():
    response = {}
    message = ""
    try:
        res = Calificacion.query.all()
        request_data = request.get_json()
        for calificacion in res:
            if (
                calificacion.data["idMovie"] == request.get_json()["data"]["idMovie"]
                and calificacion.data["idUsuario"] == request.get_json()["data"]["idUsuario"]
            ):
                message = "calificacion ya existe"
                break

        if message == "":
            calificacion = Calificacion(data=request_data["data"])
            db.session.add(calificacion)
            db.session.commit()
            response = calificacion.toJson()
            message = "calificacion agregado con exito"
    except Exception as e:
        print(e)
        print(sys.exc_info())
        message = e
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({"message": message, "response": response})


@routes.route("/likes/<int:movieID>/<int:userID>", methods=["DELETE"])
def removeLike(movieID, userID):
    message="calificacion eliminada con exito"
    try:
        res = Calificacion.query.all()
        calificacionId = 0
        for calificacion in res:
            if calificacion.data["idMovie"] == movieID and calificacion.data["idUsuario"] == userID:
                calificacionId = calificacion.id
                break
        calificacion = Calificacion.query.filter_by(id=calificacionId).first()
        db.session.delete(calificacion)
        db.session.commit()
    except Exception as e:
        print(e)
        print(sys.exc_info())
        message=e
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({"message":message})
