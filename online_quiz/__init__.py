# this is the "online_quiz/__init__.py" file...
import os
from flask import Flask

from online_quiz.routes.home_routes import home_routes
from online_quiz.routes.prequiz_routes import prequiz_routes
from online_quiz.routes.quiz_routes import quiz_routes
from online_quiz.routes.results_routes import results_routes

def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_routes)
    app.register_blueprint(prequiz_routes)
    app.register_blueprint(quiz_routes)
    app.register_blueprint(results_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)