from flask import jsonify, request
from configuration import db, sys
from models.User import User
from models.comentario import Comentario
from . import routes


@routes.route("/likes/<int:idComment>/<int:idUser>", methods=["POST"])
def addLike(idComment, idUser):
    message = ""
    try:
        comentario = Comentario.query.filter_by(id=idComment).first()
        print(comentario)
        if comentario!=None:
            for i in comentario.ilikes:
                if idUser==i.id:
                    message = "like ya existe"
                    print('igual')
                    break
        
        if message == "":
            user=User.query.filter_by(id=idUser).first()
            comentario.ilikes.append(user)
            db.session.commit()
            message = "like agregado con exito"
    except Exception as e:
        print(e)
        print(sys.exc_info())
        message = e
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({"message": message})


@routes.route("/likes/<int:idComment>/<int:idUser>", methods=["DELETE"])
def removeLike(idComment, idUser):
    message="like eliminada con exito"
    try:
        comentario = Comentario.query.filter_by(id=idComment).first()
        print(comentario.ilikes)
        for like in comentario.ilikes:
            if idUser==like.id:
                comentario.ilikes.remove(like)
                db.session.commit()
                break
        print(comentario.ilikes)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        message=e
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({"message":message})
