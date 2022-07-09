from flask import jsonify, request,abort
from configuration import db, sys
from models.User import User
from models.comentario import Comentario
from . import routes


@routes.route("/likes/<int:idComment>/<int:idUser>", methods=["POST"])
def addLike(idComment, idUser):
    message = ""
    error_404=False
    try:
        comentario = Comentario.query.filter_by(id=idComment).one_or_none()
        if comentario is None:
            error_404=True
            abort(404)
        
        if comentario != None:
            for i in comentario.ilikes:
                if idUser==i.id:
                    message = "like ya existe"
                    break
        
        if message == "":
            user=User.query.filter_by(id=idUser).one_or_none()
            if user is None:
                error_404=True
                abort(404)
            comentario.ilikes.append(user)
            total_likes=len(comentario.ilikes)
            message = "like agregado con exito"
            db.session.commit()
            return jsonify({"message": message,'success':True,'total_likes':total_likes,'id_comentario':idComment})
        else:
            return jsonify({"message": message,'success':False,'total_likes':len(comentario.ilikes),'id_comentario':idComment})
    except Exception as e:
        
        db.session.rollback()
        if error_404:
            print(e)
            abort(404)
        else:
            print(e)
            abort(500)
    finally:
        db.session.close()
    


@routes.route("/likes/<int:idComment>/<int:idUser>", methods=["DELETE"])
def removeLike(idComment, idUser):
    message="like eliminada con exito"
    error_404=False
    try:
        comentario = Comentario.query.filter_by(id=idComment).one_or_none()
        if comentario is None:
            error_404=True
            abort(404)
        for like in comentario.ilikes:
            if idUser==like.id:
                comentario.ilikes.remove(like)
                total_likes=len(comentario.ilikes)
                db.session.commit()
                break
        return jsonify({"message": message,'success':True,'total_likes':total_likes,'id_comentario':idComment})
    except Exception as e:
        print(e)
        db.session.rollback()
        if error_404:
            abort(404)
        else:
            abort(500)
    finally:
        db.session.close()
