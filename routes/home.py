from flask import render_template,session,redirect,url_for
from routes.__init__ import routes



@routes.route('/')
def home():
    if 'user' in session:
        return render_template('home/index.html',user=session['user'])
    return redirect(url_for('routes.login'))