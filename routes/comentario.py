from flask import jsonify, request
from configuration import db, sys
from models.comentario import Comentario
from routes.likes import getLikesById
from . import routes


@routes.route("/comentario/")
def getComentarios():
    res = Comentario.query.all()
    for i in range(0,len(res)):
        likes=getLikesById(res[i].id)
        res[i].data["likes"]=likes
    print(sorted(res, key=lambda x: x.data["likes"], reverse=True))
    return jsonify({"cometarios": [m.toJson() for m in res]})


@routes.route("/comentario/", methods=["POST"])
def createComentario():
    response = {}
    message = ""
    try:
        request_data = request.get_json()
        comentario = Comentario(data=request_data["data"])
        db.session.add(comentario)
        db.session.commit()
        response = comentario.toJson()
        message = "comentario agregado con exito"
    except Exception as e:
        print(e)
        print(sys.exc_info())
        message = e
        db.session.rollback()
        pass
    finally:
        db.session.close()
    return jsonify({"message": message, "response": response})

@routes.route("/movies/<int:commentID>", methods=["PUT"])
def updateComentario(commentID):
    message=""
    try:
        comentario=Comentario.query.filter_by(id=commentID).first()
        nComentario = Comentario.query.filter_by(id=commentID).update(dict(data=comentario.data))
        db.session.commit()
        message='like de Comentario actualizado con exito'
    except Exception as e:
        print(e)
        print(sys.exc_info())
        message=e
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({"message":message})

@routes.route("/movies/<int:commentID>", methods=["DELETE"])
def deleteComentario(commentID):
    message = ""
    try:
        comentario = Comentario.query.filter_by(id=commentID).first()
        db.session.delete(comentario)
        db.session.commit()
        message = "comentario eliminada con exito"
    except Exception as e:
        print(e)
        print(sys.exc_info())
        message = e
        db.session.rollback()
    finally:
        db.session.close()

    return jsonify({"message": message})
