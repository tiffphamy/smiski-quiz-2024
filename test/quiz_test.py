from flask import Flask
from web_app.routes.quiz_routes import quiz_routes

def test_quiz_route(client):
    # Test the /quiz route
    response = client.get("/quiz")
    assert response.status_code == 200
    assert b"SMISKI QUIZ..." in response.data