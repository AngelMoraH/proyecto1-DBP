from flask import Flask
from dotenv import load_dotenv
import os
from routes import *
from configuration import db,jsf


app = Flask(__name__)  # dander-name meta data
load_dotenv(".env")
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{os.environ.get('USER')}:{os.environ.get('PASSWORD')}@{os.environ.get('HOST')}:{os.environ.get('PORT')}/{os.environ.get('DB')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.environ.get("API_SECRETE_KEY")
app.register_blueprint(routes,url_prefix="/")
db.init_app(app)


with app.app_context():
    db.create_all()


# run
if __name__ == "__main__":
    app.run(debug=True)
