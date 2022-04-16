from flask import render_template,request,redirect,url_for,session
from werkzeug.security import check_password_hash,generate_password_hash
import datetime
from configuration import db
from models.User import User
from . import routes

@routes.route('/')
def index():
    if 'user' in session:
        return render_template('index.html',user=session['user'])
    return redirect(url_for('routes.login'))

@routes.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        user=db.session.query(User).filter_by(email=request.form['email']).first()
        if check_password_hash(user.password,request.form['password']):
            session['user']=user.toJson()
            return redirect(url_for("routes.index"))
        else:
            return "error"
    else:
        return render_template("auth/login.html")


@routes.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for("routes.index"))


@routes.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        user = User(
        userName=request.form['userName'],
        email=request.form['email'],
        password=   generate_password_hash(request.form['password']),
        dateCreated=datetime.datetime.now(),
        )
        db.session.add(user)
        db.session.commit()
        db.session.close()
        return redirect(url_for("home"))
    else:
        return render_template("auth/register.html")
    