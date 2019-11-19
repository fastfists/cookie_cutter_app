from .models import User
from .views import user

def init_app(app):
    app.register_blueprint(user)
