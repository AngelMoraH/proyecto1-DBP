from flask import Blueprint
routes = Blueprint('routes', __name__)

from .users import *
from .movies import *
from .likes import *
from .comentario import *