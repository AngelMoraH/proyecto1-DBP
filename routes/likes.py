from flask import Response, request
from configuration import db
from models.Likes import Likes
from . import routes


@routes.route("/likes/")
def getLikes():
    res = Likes.query.all()
    likes = {}
    likes["likes"] = []
    for like in res:
        likes["likes"].append(like.toJson())
    return Response(str(likes["likes"]))


@routes.route("/likes/", methods=["POST"])
def addLike():
    request_data = request.get_json()
    like = Likes(
        idMovie=request_data["idMovie"],
        idUsuario=request_data["idUsuario"],
        boolLike=request_data["boolLike"],
        dateCreated=request_data["dateCreated"],
    )
    db.session.add(like)
    db.session.commit()
    db.session.close()
    return "like hecho con exito"

@routes.route("/likes/<int:movieID>/<int:userID>", methods=["DELETE"])
def removeLike(movieID,userID):
    like = Likes.query.filter_by(idMovie=movieID,idUsuario=userID).first()
    db.session.delete(like)
    db.session.commit()
    db.session.close()
    return "like eliminada con exito"