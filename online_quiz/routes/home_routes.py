# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template
from app.smiski_quiz import Image, display

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return render_template("home.html")

@home_routes.route("/prequiz")
def prequiz():
    print("PREQUIZ...")
    return render_template("prequiz.html")

@home_routes.route("/map")
def map():
    print("MAP...")
    return render_template("map.html")
