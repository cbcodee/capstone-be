from flask import Flask, request, url_for, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from flask_cors import CORS
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()



def create_app(test_config=None):
        app = Flask(__name__)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
                "SQLALCHEMY_DATABASE_URI")
        
        # app.config['SECRET_KEY'] = os.urandom(64)
        # app.config['SESSION_TYPE'] = 'filesystem'
        # app.config['SESSION_FILE_DIR'] = './.flask_session/'
        

        db.init_app(app)
        migrate.init_app(app, db)
        
        # Import models here for Alembic setup
        from app.models.task import Task
        from app.models.user import User

        # Register Blueprints here
        
        from .routes import task
        from .routes import user_routes
        app.register_blueprint(task.task_bp)
        app.register_blueprint(user_routes.user_bp)
        # from .routes import spotify_route
        # app.register_blueprint(spotify_route.spotify_bp)



        # app.config["SESSION_COOKIE_NAME"] = "Cristals Cookie"
        app.config['CORS_HEADERS'] = 'Content-Type'
        CORS(app)
        return app
