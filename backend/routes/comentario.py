from distutils.log import error
from functools import total_ordering
from flask import jsonify, request, abort
from models.Movies import Movie
from configuration import db
from models.comentario import Comentario, ComentarioPadre, ComentarioHijo
from . import routes
import http
from datetime import datetime



@routes.route("/comentarios/<int:movieID>")
def getComentario(movieID):
    status_code = 0
    res = Comentario.query.all()
    movie = Movie.query.filter_by(id=movieID).one_or_none()
    if movie is None:
        abort(404)
    for i in range(0, len(res)):
        res[i].data["likes"] = len(Comentario.query.filter_by(id=res[i].id).first().ilikes)
    sorted(res, key=lambda x: x.data["likes"], reverse=True)
    status_code = http.HTTPStatus.ACCEPTED
    return jsonify(
        {"comentarios": [m.toJson() for m in res if m.data['idMovie'] == movieID],"total_comentarios": len(res), "status_code": status_code, 'success':True})


@routes.route("/comentarios", methods=["POST"])
def createComentario():
    comentario = {}
    message = ""
    status_code = 0
    error_404=False
    error_422=False
    try:
        body = request.get_json()
        data = body.get("data", None)
        
        if data is None:
            error_422 = True
            abort(422)
        data['dateCreated'] = datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')
        comentario = Comentario(data=data)
        total_comentarios=Comentario.query.all()
        db.session.add(comentario)
        db.session.commit()
        comentariores = comentario.toJson()
        message = "comentario agregado con exito"
        status_code = http.HTTPStatus.ACCEPTED
        return jsonify({
            "message": message, 
            "comentario": comentariores,
            "comentario_id":comentariores['id'],
            "total_comentarios": len(total_comentarios),
            'success': True
        })
    except Exception as e:
        
        db.session.rollback()
        if error_422:
            abort(422)
        else:
            abort(500)
    finally:
        db.session.close()
    


@routes.route("/comentarios/<int:commentID>", methods=["PUT"])
def updateComentario(commentID):
    message = ""
    status_code = 0
    error_404=False
    error_422=False
    try:
        body = request.get_json()
        comentarioDATA = body.get("data",None)
        if comentarioDATA is None:
            error_422 = True
            abort(422)
            
        comentario = Comentario.query.filter_by(id=commentID).one_or_none()
        if comentario is None:
            error_404=True
            abort(404)
            
        nComentario = Comentario.query.filter_by(id=commentID).update(dict(data=comentarioDATA))

        db.session.commit()
        message = 'Comentario actualizado con exito'
        return jsonify({
            "message": message, 
            'success': True,
            'id': commentID
        })
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
    


@routes.route("/comentarios/<int:commentID>/<int:userID>", methods=["DELETE"])
def deleteComentario(commentID, userID):
    message = ""
    error = False
    status_code = 0
    error_404=False
    try:
        comentario = Comentario.query.filter_by(id=commentID).one_or_none()
        if comentario is None:
                error_404 = True
                abort(404)
        comentarios=Comentario.query.all()
        if comentario.data['idUser'] == userID:
            db.session.delete(comentario)
            db.session.commit()
            return jsonify({
                'success': True,
                'deleted': commentID,
                'total_comentarios': len(comentarios),
                'status_code':200
            })
        else:
            return jsonify({
                'message':"usuario no autorizado",
                'success': False,
                'status_code':http.HTTPStatus.UNAUTHORIZED
            })
    except Exception as e:
        db.session.rollback()
        if error_404:
            abort(404)
        else:
            abort(500)
    finally:
        db.session.close()
