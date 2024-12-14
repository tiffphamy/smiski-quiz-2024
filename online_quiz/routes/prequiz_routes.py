from flask import Blueprint, request, render_template
from app.smiski_quiz import Image, display

prequiz_routes = Blueprint("prequiz_routes", __name__)

@prequiz_routes.route("/prequiz")
def prequiz():
    print("SMISKI PREQUIZ...")
    return render_template("prequiz.html")