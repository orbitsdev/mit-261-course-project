from flask import Blueprint

registrar_bp = Blueprint('registrar_bp', __name__, template_folder='templates')

from . import routes  # binds the routes to blueprint
