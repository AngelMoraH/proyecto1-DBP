from flask import abort, jsonify, render_template,request,redirect,url_for,session
from werkzeug.security import check_password_hash,generate_password_hash
import datetime
import http
from configuration import db,sys
from models.User import User
from . import routes


@routes.route("/user/<int:userID>", methods=["GET"])
def getUserById(userID):
    error_404=0
    try:
        user= User.query.filter_by(id=userID).one_or_none()
        if user is None:
            error_404=True
            abort(404)
        return jsonify({'success':True,'status_code':http.HTTPStatus.OK,'user':user.toJson()})
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)

@routes.route('/login/',methods=["POST"])
def login():
    status_code=0
    error_404 = False
    try:
        body = request.get_json()
        print(body)
        user=User.query.filter_by(email=body.get('email')).one_or_none()
        if user is None:
            error_404= True
            abort(404)
        if user:
            if check_password_hash(user.password,body.get('password')):
                session['user']=user.toJson()
                status_code=http.HTTPStatus.OK
                return jsonify({
                    "user":user.toJson(),
                    "success":True,
                    "status_code":status_code
                })
            else:
                status_code=http.HTTPStatus.BAD_REQUEST
                return jsonify({
                    "message":"Usuario o contraseña incorrectos",
                    "success":False,
                    "status_code":status_code
                })
        else:
            status_code=http.HTTPStatus.BAD_REQUEST
            return jsonify({
                "message":"Usuario no existe",
                "success":False,
                "status_code":status_code
            })
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)


@routes.route("/logout")
def logout():
    session.pop('user', None)
    return jsonify({
        "success":True,
        "status_code":http.HTTPStatus.OK
    })


@routes.route("/register",methods=["POST"])
def register():
    response={}
    body = request.get_json()
    userName= body.get('userName',None)
    email= body.get('email',None)
    password=generate_password_hash(body.get('password',None))
    
    if userName is None or email is None or password is None:
        abort(422)
    try:
        user = User(
        userName= userName,
        email= email,
        password=password,
        dateCreated=datetime.datetime.now(),
        )
        db.session.add(user)
        db.session.commit()
        response['success']=True
        response['status_code']= http.HTTPStatus.ACCEPTED
        response['message']="Usuario agregado con exito"
    except Exception as e:
        print(e)
        print(sys.exc_info())
        db.session.rollback()
        response['success']=False
        response['status_code']= http.HTTPStatus.BAD_REQUEST
        response['message']="No se pudo registrar el usuario"
    finally:
        db.session.close()
    return jsonify({
        'message':response["message"],
        'success':response["success"],
        "status_code":response["status_code"]
    })