from flask import Blueprint, request, render_template
from app.smiski_quiz import image, display

quiz_routes = Blueprint("quiz_routes", __name__)

@quiz_routes.route("/quiz")
def quiz():
    print("SMISKI QUIZ...")

    questions = [
        {
            "question": "Question 1: How do you like to spend your free time?",
            "options": [
                "a) Imagining wild scenarios and daydreaming about 'what could be.'", 
                "b) Dancing, singing, or just finding ways to add a little fun to the moment.",
                "c) Curling up somewhere cozy for a much-needed nap.", 
                "d) Thinking through big ideas and solving life's little mysteries."
            ]
        },
        {
            "question": "Question 2: What is your go-to vibe in a group setting?",
            "options": [
                "a) Quietly observing from the sidelines—you like to keep things low-key.",
                "b) Jumping in to entertain and make everyone smile—you’re the fun one!",
                "c) Offering thoughtful advice or coming up with a genius plan.",
                "d) Helping wherever you’re needed—lifting the mood or literal furniture!"
            ]
        },
        {
            "question": "Question 3: If your friends described you in one word, what would it be?",
            "options": [
                "a) Dreamy—you’re always off in your own little world.",
                "b) Playful—you bring energy and joy wherever you go.",
                "c) Relaxed—you’re a chill presence who loves to recharge.",
                "d) Strong—you’re dependable, resilient, and there when it counts."
            ]
        },
        {
            "question": "Question 4: What’s your ideal environment?",
            "options": [
                "a) A cozy corner where you can quietly reflect or observe.",
                "b) A lively space with lots of energy and good vibes.",
                "c) Anywhere with soft blankets and a place to snooze.",
                "d) Somewhere you can think, create, or tackle challenges."
            ]
        },
        {
            "question": "Question 5: How do you usually approach a problem?",
            "options": [
                "a) By brainstorming creative solutions and imagining the possibilities.",
                "b) By jumping in with enthusiasm and keeping it upbeat.",
                "c) By staying calm, assessing the situation, and taking your time.",
                "d) By tackling it head-on with focus and determination."
            ]
        },
        {
            "question": "Question 6: What’s your ultimate self-care routine?",
            "options": [
                "a) Letting your mind wander with a good book or journaling.",
                "b) Doing something fun like dancing or catching up with friends.",
                "c) Relaxing in your favorite spot with cozy vibes all around.",
                "d) Engaging in a project or hobby that recharges your energy."
            ]
        },
        {
            "question": "Question 7: What type of adventure appeals to you most?",
            "options": [
                "a) A quiet retreat where you can explore new ideas and reflect.",
                "b) A lively road trip with spontaneous stops and laughter.",
                "c) A laid-back beach day with no plans but to unwind.",
                "d) An active challenge."
            ]
        }
    ]

    return render_template("quiz.html")