# Flask Project Structure Guide

This is a recommended folder and file layout for scalable Flask projects.
It follows the MVC pattern and includes support for blueprints, static files, templates, uploads, and helper modules.

## 🗂 Folder Structure

```
my_flask_project/
│
├── .venv/                            # Virtual environment (do not commit to Git)
├── app.py                            # Entry point of the application
├── config.py                         # App-wide config file (e.g., for Flask config vars)
├── requirements.txt                  # Python dependencies list
├── README.md                         # Project overview
│
├── instance/                         # Local-only settings (e.g., dev DB)
│   └── config.py
│
├── app/                              # Main application code
│   ├── __init__.py                   # App factory & blueprint registration
│   │
│   ├── models/                       # Database models (e.g., SQLAlchemy)
│   │   └── user.py
│   │   └── post.py
│   │
│   ├── routes/                       # Modularized route definitions (Blueprnts)
│   │   └── __init__.py
│   │   └── home.py
│   │   └── auth.py
│   │   └── dashboard.py
│   │
│   ├── templates/                    # HTML templates (Jinja2)
│   │   ├── base.html                 # Base layout template
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── dashboard/
│   │   │   └── index.html
│   │   └── includes/                # Shared HTML components (navbar, footer)
│   │       ├── navbar.html
│   │       └── footer.html
│   │
│   ├── static/                       # Static files (CSS, JS, images)
│   │   ├── css/
│   │   │   └── main.css
│   │   ├── js/
│   │   │   └── app.js
│   │   └── images/
│   │       ├── logo.png
│   │       └── user-placeholder.png
│   │
│   ├── uploads/                      # Uploaded user files (images, PDFs, etc.)
│   │   └── sample.pdf
│   │
│   ├── forms/                        # Flask-WTF form classes
│   │   └── login_form.py
│   │   └── register_form.py
│   │
│   ├── utils/                        # Reusable utility functions
│   │   └── file_utils.py
│   │   └── auth_helpers.py
│   │
│   └── extensions.py                # External extensions init (e.g., db, bcrypt)
```

## 📌 Key File Roles

- **app.py**: Main entry point (runs the app)
- **app/__init__.py**: Initializes Flask app, loads config, registers blueprints
- **routes/**: Groups route logic per feature (modular)
- **templates/**: HTML views using Jinja2
- **static/**: Frontend assets (CSS, JS, images)
- **uploads/**: Files uploaded by users (must be manually exposed via route)
- **forms/**: Input forms using Flask-WTF
- **utils/**: Helper functions (e.g., password hashing, date formatters)
- **extensions.py**: Used to init 3rd-party tools (e.g., `SQLAlchemy()`)

## ✅ Tips

- Use `url_for('static', filename='images/logo.png')` for images in templates.
- Use Blueprints to keep feature routes organized.
- Add `.venv/` and `__pycache__/` to `.gitignore`.
- Use `requirements.txt` to track packages (`pip freeze > requirements.txt`).
- Always use a virtual environment!

---

Happy coding with Flask 🚀