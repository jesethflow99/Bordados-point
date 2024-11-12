from flask import Flask
from app.bp.auth.routes import auth
from app.bp.dashboard.routes import dashboard
from app.config import Config
from app.models import db


def Create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    db.init_app(app)
    
    return app