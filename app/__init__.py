from flask import Flask
from .routes.book_routes import books_bp
#from .routes.hello_world_routes import hello_world_bp #Not needed for hello books API
from .db import db, migrate #Imports the db and migrate objects we created previously
from .models import book # Newly added import
import os




def create_app(config=None):
    app = Flask(__name__)

    #hide a warning about a feature in SQLAlchemy that we won't be using.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    #set to the connection string for our database
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        # Merge `config` into the app's configuration
        # to override the app's default settings
        app.config.update(config)

    #Connects db and migrate to our Flask app, using the package's recommended syntax. 
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(books_bp)
    # This code not needed for hello books API
    #app.register_blueprint(hello_world_bp)
    
    return app
