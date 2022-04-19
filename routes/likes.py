from flask import Response, request
from configuration import db
from models.Likes import Likes
from . import routes


@routes.route("/likes/")
def getLikes():
    res = Likes.query.all()
    return Response(str(res))


@routes.route("/likes/", methods=["POST"])
def addLike():
    res = Likes.query.all()
    response = ""
    request_data = request.get_json()
    print(request_data["data"]["idMovie"])
    for like in res:
        if (
            like.data["idMovie"] == request_data["data"]["idMovie"]
            and like.data["idUsuario"] == request_data["data"]["idUsuario"]
        ):
            response = "like ya existe"
            break

    if response != "":
        return response
    else:
        like = Likes(data=request_data["data"])
        db.session.add(like)
        db.session.commit()
        db.session.close()
        return "like hecho con exito"


@routes.route("/likes/<int:movieID>/<int:userID>", methods=["DELETE"])
def removeLike(movieID, userID):
    res = Likes.query.all()
    likeId = 0
    for like in res:
        if like.data["idMovie"] == movieID and like.data["idUsuario"] == userID:
            likeId = like.id
            break
    like = Likes.query.filter_by(id=likeId).first()
    db.session.delete(like)
    db.session.commit()
    db.session.close()
    return "like eliminada con exito"
