from . import faculty_bp
from flask import render_template

@faculty_bp.route('/')
def index():
    return render_template('index.html')