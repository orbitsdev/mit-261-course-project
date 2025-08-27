from flask import Blueprint

faculty_bp = Blueprint('faculty_bp', __name__, template_folder='templates', url_prefix='/faculty')

from . import routes  # binds the routes to blueprint
