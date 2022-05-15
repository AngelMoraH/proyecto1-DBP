from flask import jsonify, request,abort
from configuration import db
from models.comentario import Comentario
from . import routes
import http
from datetime import datetime

@routes.route("/comentario/<int:movieID>")
def getComentarios(movieID):
    status_code=0
    res = Comentario.query.all()
    for i in range(0,len(res)):
        res[i].data["likes"]=len(Comentario.query.filter_by(id=res[i].id).first().ilikes)
    sorted(res, key=lambda x: x.data["likes"], reverse=True)
    status_code =http.HTTPStatus.ACCEPTED
    return jsonify({"comentarios": [m.toJson() for m in res if m.data['idMovie']== movieID],"status_code":status_code})	



@routes.route("/comentario/", methods=["POST"])
def createComentario():
    response = {}
    message = ""
    status_code=0
    try:
        request_data = request.get_data().decode('utf-8')
        data1=request_data[9:len(request_data)-2].split(",")
        for i in range(0,len(data1)):
            data1[i]=data1[i].split(":")
        resDATA={
            data1[0][0][1:len(data1[0][0])-1]:data1[0][1][1:len(data1[0][1])-1],
            data1[1][0][1:len(data1[1][0])-1]:int(data1[1][1]),
            data1[2][0][1:len(data1[2][0])-1]:int(data1[2][1]),
            data1[3][0][1:len(data1[3][0])-1]:datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        }
        comentario = Comentario(data=resDATA)
        db.session.add(comentario)
        db.session.commit()
        response = comentario.toJson()
        message = "comentario agregado con exito"
        status_code =http.HTTPStatus.ACCEPTED
    except Exception as e:
        print(e)
        db.session.rollback()
        status_code =http.HTTPStatus.INTERNAL_SERVER_ERROR
        abort(status_code)
    finally:
        db.session.close()
    return jsonify({"message": message, "response": response, "status_code": status_code})

@routes.route("/comentario/<int:commentID>", methods=["PUT"])
def updateComentario(commentID):
    message=""
    status_code=0
    try:
        comentarioDATA=request.get_json()["data"]
        nComentario = Comentario.query.filter_by(id=commentID).update(dict(data=comentarioDATA))
        db.session.commit()
        message='like de Comentario actualizado con exito'
    except Exception as e:
        print(e)
        db.session.rollback()
        status_code =http.HTTPStatus.INTERNAL_SERVER_ERROR
        abort(status_code)
    finally:
        db.session.close()
    return jsonify({"message":message,'status_code':status_code})

@routes.route("/comentario/<int:commentID>/<int:userID>", methods=["DELETE"])
def deleteComentario(commentID,userID):
    message = ""
    error = False
    status_code=0
    try:
        comentario = Comentario.query.filter_by(id=commentID).first()
        if comentario.data['idUser']==userID:
            db.session.delete(comentario)
            db.session.commit()
            message = "comentario eliminada con exito"
            status_code = http.HTTPStatus.ACCEPTED
        else:
            message = "usuario no autorizado"
    except Exception as e:
        db.session.rollback()
        error=True
        status_code = http.HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        db.session.close()
    if error == True:
        abort(status_code)
    return jsonify({"message": message,'status_code':status_code})
