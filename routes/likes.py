from flask import jsonify, request,session
from configuration import db, sys
from models.Likes import Likes
from . import routes


@routes.route("/likes/")
def getLikes():
    res = Likes.query.all()
    return jsonify({"likes": [l.toJson() for l in res]})


@routes.route("/likes/<int:commentID>/")
def getLikesById(commentID):
    try:
        res = Likes.query.all()
        totalLikes = 0
        for like in res:
            if like.data["idComment"] == commentID:
                totalLikes += 1
    except Exception as e:
        print(e)
        print(sys.exc_info())

    return totalLikes #jsonify({"likes": totalLikes})


@routes.route("/likes/", methods=["POST"])
def addLike():
    response = {}
    message = ""
    try:
        res = Likes.query.all()
        request_data = request.get_json()
        for like in res:
            if (
                like.data["idComment"] == request.get_json()["data"]["idComment"]
                and like.data["idUsuario"] == request.get_json()["data"]["idUsuario"]
            ):
                message = "like ya existe"
                break

        if message == "":
            like = Likes(data=request_data["data"])
            db.session.add(like)
            db.session.commit()
            response = like.toJson()
            message = "like agregado con exito"
    except Exception as e:
        print(e)
        print(sys.exc_info())
        message = e
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({"message": message, "response": response})


@routes.route("/likes/<int:commentID>/<int:userID>", methods=["DELETE"])
def removeLike(commentID, userID):
    message="like eliminada con exito"
    try:
        res = Likes.query.all()
        likeId = 0
        for like in res:
            if like.data["idComment"] == commentID and like.data["idUsuario"] == userID:
                likeId = like.id
                break
        like = Likes.query.filter_by(id=likeId).first()
        db.session.delete(like)
        db.session.commit()
    except Exception as e:
        print(e)
        print(sys.exc_info())
        message=e
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({"message":message})
