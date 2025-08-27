from flask import Flask
from .students import student_bp
from .faculty import faculty_bp
from .registrar import registrar_bp

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(student_bp, url_prefix='/students')
    app.register_blueprint(faculty_bp, url_prefix='/faculty')
    app.register_blueprint(registrar_bp, url_prefix='/registrar')

    return app
