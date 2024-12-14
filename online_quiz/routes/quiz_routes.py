from flask import Blueprint, request, render_template
from app.smiski_quiz import Image, display

quiz_routes = Blueprint("quiz_routes", __name__)

questions = [
    {
        "question": "Question 1: How do you like to spend your free time?",
        "options": {
            "a": "a) Imagining wild scenarios and daydreaming about 'what could be.'",
            "b": "b) Dancing, singing, or just finding ways to add a little fun to the moment.",
            "c": "c) Curling up somewhere cozy for a much-needed nap.",
            "d": "d) Thinking through big ideas and solving life's little mysteries."
        },
        "name": "1"
    },
    {
        "question": "Question 2: What is your go-to vibe in a group setting?",
        "options": {
            "a": "a) Quietly observing from the sidelines—you like to keep things low-key.",
            "b": "b) Jumping in to entertain and make everyone smile—you’re the fun one!",
            "c": "c) Offering thoughtful advice or coming up with a genius plan.",
            "d": "d) Helping wherever you're needed—lifting the mood or literal furniture!"
        },
        "name": "2"
    },
    {
        "question": "Question 3: If your friends described you in one word, what would it be?",
        "options": {
            "a": "a) Dreamy—you're always off in your own little world.",
            "b": "b) Playful—you bring energy and joy wherever you go.",
            "c": "c) Relaxed—you're a chill presence who loves to recharge.",
            "d": "d) Strong—you're dependable, resilient, and there when it counts."
        },
        "name": "3"
    },
    {
        "question": "Question 4: What's your ideal environment?",
        "options": {
            "a": "a) A cozy corner where you can quietly reflect or observe.",
            "b": "b) A lively space with lots of energy and good vibes.",
            "c": "c) Anywhere with soft blankets and a place to snooze.",
            "d": "d) Somewhere you can think, create, or tackle challenges."
        },
        "name": "4"
    },
    {
        "question": "Question 5: How do you usually approach a problem?",
        "options": {
            "a": "a) By brainstorming creative solutions and imagining the possibilities.",
            "b": "b) By jumping in with enthusiasm and keeping it upbeat.",
            "c": "c) By staying calm, assessing the situation, and taking your time.",
            "d": "d) By tackling it head-on with focus and determination."
        },
        "name": "5"
    },
    {
        "question": "Question 6: What's your ultimate self-care routine?",
        "options": {
            "a": "a) Letting your mind wander with a good book or journaling.",
            "b": "b) Doing something fun like dancing or catching up with friends.",
            "c": "c) Relaxing in your favorite spot with cozy vibes all around.",
            "d": "d) Engaging in a project or hobby that recharges your energy."
        },
        "name": "6"
    },
    {
        "question": "Question 7: What type of adventure appeals to you most?",
        "options": {
            "a": "a) A quiet retreat where you can explore new ideas and reflect.",
            "b": "b) A lively road trip with spontaneous stops and laughter.",
            "c": "c) A laid-back beach day with no plans but to unwind.",
            "d": "d) An active challenge."
        },
        "name": "7"
    }
]

@quiz_routes.route("/quiz", methods=["GET"])
def quiz():
    return render_template('quiz.html', questions=questions)

@quiz_routes.route("/results", methods=["POST"])
def quiz_results():
    answers = request.form
    answer_list = list(answers.values())  # Get submitted answers
    counters = {"A": 0, "B": 0, "C": 0, "D": 0}
    
    for answer in answer_list:
        if answer.upper() in counters:
            counters[answer.upper()] += 1

    return render_template("result.html", result=result)