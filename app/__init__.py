from flask import Flask
from .routes.book_routes import books_bp
#from .routes.hello_world_routes import hello_world_bp #Not needed for hello books API

def create_app():
    app = Flask(__name__)

    # Register Blueprints here
    app.register_blueprint(books_bp)
    # This code not needed for hello books API
    #app.register_blueprint(hello_world_bp)
    
    return app
