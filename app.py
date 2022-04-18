from flask import Flask
from dotenv import load_dotenv
import os
from routes import *
from configuration import db


app = Flask(__name__)  # dander-name meta data
load_dotenv(".env")
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://postgres:{os.environ.get('PASSWORD')}@localhost:{os.environ.get('PORT')}/proyecto1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.environ.get("API_SECRETE_KEY")
app.register_blueprint(routes,url_prefix="/")
db.init_app(app)


with app.app_context():
    db.create_all()


# run
if __name__ == "__main__":
    app.run(debug=True)
