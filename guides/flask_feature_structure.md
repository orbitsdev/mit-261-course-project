# Flask Feature-Based Project Structure (Modular MVC Style)

This structure is designed for medium to large Flask projects that separate functionality per **feature** (e.g., student, faculty, registrar).

---

## 📁 Project Structure

```
my_flask_project/
├── app.py                    # Entry point for running the Flask app
├── requirements.txt
├── config.py                 # Global config (can be split per environment)
│
├── app/                      # Main app package
│   ├── __init__.py           # App factory + blueprint registration
│   ├── extensions.py         # Shared tools (e.g. db, login manager)
│   ├── templates/            # Shared global templates (base.html, layout)
│   ├── static/               # Shared static files (CSS, JS, images)
│
│   ├── student/              # 🎓 Student feature module
│   │   ├── __init__.py       # Defines and registers student blueprint
│   │   ├── routes.py         # Student routes (controllers)
│   │   ├── models.py         # Student-specific DB models
│   │   ├── forms.py          # Student input forms
│   │   └── templates/
│   │       └── student/
│   │           └── dashboard.html
│
│   ├── faculty/              # 🧑‍🏫 Faculty feature module
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   ├── forms.py
│   │   └── templates/
│   │       └── faculty/
│   │           └── dashboard.html
│
│   ├── registrar/            # 🧾 Registrar feature module
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   ├── forms.py
│   │   └── templates/
│   │       └── registrar/
│   │           └── index.html
│
│   └── shared/               # Shared helpers/utilities
│       ├── utils.py
│       ├── decorators.py
│       └── forms.py
```

---

## 🧠 File Purpose Overview

| File/Folder     | Purpose                                                      |
|-----------------|--------------------------------------------------------------|
| `routes.py`     | Handles URL routing and view logic (controllers)             |
| `models.py`     | Database schema for each feature                             |
| `forms.py`      | Flask-WTF form handling and validation                       |
| `templates/`    | HTML views grouped per feature (uses Jinja2 templating)      |
| `__init__.py`   | Initializes each module and registers it as a blueprint      |
| `shared/`       | Utility functions reusable by all features                   |
| `extensions.py` | Flask extensions like `db = SQLAlchemy()`, etc.              |

---

## 🧩 Routing Example (student/routes.py)

```python
from . import student_bp
from flask import render_template

@student_bp.route("/dashboard")
def dashboard():
    return render_template("student/dashboard.html")
```

And in `student/__init__.py`:

```python
from flask import Blueprint

student_bp = Blueprint("student", __name__, template_folder="templates")

from . import routes  # important to bind the routes
```

---

## 🧱 App Factory (app/__init__.py)

```python
from flask import Flask
from .student import student_bp
from .faculty import faculty_bp
from .registrar import registrar_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(student_bp, url_prefix="/student")
    app.register_blueprint(faculty_bp, url_prefix="/faculty")
    app.register_blueprint(registrar_bp, url_prefix="/registrar")
    return app
```

---

## ✅ Tips

- Always group logic by feature for larger projects
- Reuse code via `shared/` or `common/` folders
- Use `url_prefix="/..."` in `register_blueprint()` to keep routes clean
- Keep template folder paths matched to feature (e.g., `templates/student/`)

---

This structure helps you scale, maintain, and organize Flask apps like a professional.