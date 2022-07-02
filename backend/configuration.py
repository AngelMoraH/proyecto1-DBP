import sys
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


database_name = "practica"
load_dotenv(".env")

database_path = "postgresql://{}:{}@{}:{}/{}".format(os.environ.get("USER"), os.environ.get("PASSWORD"), os.environ.get("HOST"), os.environ.get("PORT"), os.environ.get("DATABASE_NAME"))
#database_path='postgresql://{}:{}@{}/{}'.format('postgres','dev123', 'localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    app.secret_key = os.environ.get("API_SECRETE_KEY")
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    # db.create_all()
