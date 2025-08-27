from . import student_bp
from flask import render_template

@student_bp.route('/')
def index():
    return render_template('student.html')
