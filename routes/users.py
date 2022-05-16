from flask import jsonify, render_template,request,redirect,url_for,session
from werkzeug.security import check_password_hash,generate_password_hash
import datetime
import http
from configuration import db,sys
from models.User import User
from . import routes


@routes.route("/getUser/<int:userID>", methods=["GET"])
def getUserById(userID):
    user=User.query.filter_by(id=userID).first()
    return jsonify({'user':user.toJson()})

@routes.route('/login/',methods=["GET","POST"])
def login():
    status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR
    if request.method == "POST":
        user=User.query.filter_by(email=request.get_json()['email']).first()
        if user:
            if check_password_hash(user.password,request.get_json()['password']):
                session['user']=user.toJson()
                status_code=http.HTTPStatus.OK
                return jsonify({"user":user.toJson(),"status":"success","status_code":status_code})
            else:
                return jsonify({"message":"Usuario o contraseña incorrectos","status":"no success","status_code":status_code})
        else:
            return jsonify({"message":"Usuario no existe","status":"no success","status_code":status_code})
    else:
        return render_template("auth/login.html")


@routes.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for("routes.home"))


@routes.route("/register",methods=["GET","POST"])
def register():
    response={}
    if request.method == "POST":
        try:
            user = User(
            userName=request.get_json()['userName'],
            email=request.get_json()['email'],
            password=generate_password_hash(request.get_json()['password']),
            dateCreated=datetime.datetime.now(),
            )
            db.session.add(user)
            db.session.commit()
            response['user']=user.toJson()
            response['status']="success"
            response['status_code']= http.HTTPStatus.ACCEPTED
            response['message']="Usuario agregado con exito"
        except Exception as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            response['status']="no success"
            response['status_code']= http.HTTPStatus.INTERNAL_SERVER_ERROR
            response['message']="No se pudo registrar el usuario"
        finally:
            db.session.close()
        return jsonify({'message':response["message"],'status':response["status"],"status_code":response["status_code"],"user":response["user"]})
    else:
        return render_template("auth/register.html")
    