# this is the "web_app/__init__.py" file...
import os
from flask import Flask

#from web_app.routes.smiski_routes import smiski_routes
from online_quiz.routes.home_routes import home_routes

def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_routes)
    #app.register_blueprint(smiski_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)