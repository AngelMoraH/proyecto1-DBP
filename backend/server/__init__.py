from flask import (
    Flask,
)
import os
from routes import *
from flask_cors import CORS
from configuration import setup_db


def create_app(test_config=None):
    app = Flask(__name__, template_folder='../templates')
    setup_db(app)
    CORS(app,origins=['*'],max_age=10)
    app.register_blueprint(routes, url_prefix="/")
    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'code': 404,
            'message': 'resource not found'
        }),404
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'code': 500,
            'message': 'Internal server error'
        }),500
    
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'code': 422,
            'message': 'Unprocessable'
        }),422
    
    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False,
            'code': 403,
            'message': 'Forbidden'
        }),403
    
    return app

# $env:FLASK_APP = 'server'
# $env:FLASK_ENV = 'development'
# flask run