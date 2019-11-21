from flask import Flask


def create_app(config_object='src.settings') -> Flask:
    from . import user
    from . import public

    app = Flask(__name__)
    app.config.from_object(config_object)
    
    user.init_app(app)
    public.init_app(app)

    return app

def register_extensions(app):
    from src.ext import migrate, ma, admin, db, sekazi, login_manager, bcrypt

    db.init_app(app)
    db.app = app

    login_manager.init_app(app)
    sekazi.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    bcrypt.init_app(app)

