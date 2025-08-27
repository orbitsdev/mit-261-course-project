from . import registrar_bp
from flask import render_template

@registrar_bp.route('/')
def index():
    return render_template('index.html')