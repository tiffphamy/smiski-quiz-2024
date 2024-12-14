from flask import Blueprint, request, render_template
from app.smiski_quiz import Image, display
from collections import Counter

results_routes = Blueprint("results_routes", __name__)

smiski_results = [
    {
        "smiski": "SMISKI DAYDREAMING",
        "description": "You're a whimsical wanderer, lost in the clouds but somehow always on time for dessert.\n"
            "Your imagination is your playground, and you're never short of quirky ideas or 'what if' scenarios.\n"
            "Whether it's pondering life's mysteries or deciding what the moon smells like, you're a creative soul who sees the world through a unique lens.\n"
            "Sure, you might forget where you put your keys (again), but you've probably already envisioned a secret portal hidden in the couch cushions anyway.\n"
            "Keep dreaming, you delightful daydreamer—you're proof that a little whimsy makes the world brighter!\n",
        "url": "https://blinkbox.com.au/cdn/shop/files/smiski_living-series_individual-daydreaming.webp?v=1706054580&width=1406"
    },
    {
        "smiski": "SMISKI PLAYING",
        "description": "You're the life of the invisible party, a joyful creator who turns even the quietest moments into a celebration. \n"
           "Whether it's tapping out rhythms on a desk or choreographing secret dance moves in the kitchen, you find delight in simple pleasures. \n"
           "Others can't help but smile when they're around you—your energy is contagious! \n"
           "Keep playing your unique tune, you maestro of mischief.",
        "url": "https://blinkbox.com.au/cdn/shop/files/smiski_living-series_individual-playing.webp?v=1706086015&width=1406"
    },
    {
        "smiski": "SMISKI NAP TIME",
        "description": "A true champion of rest and relaxation, you've mastered the art of doing nothing—and doing it well.\n"
            "Whether it's a 10-minute snooze or a full-blown nap marathon, you know that recharging is the secret to\n"
            "your brilliance. Some might call you “lazy,” but you call it “energy management.” Dream big, nap often,\n"
            "and keep being unapologetically chill.",
        "url": "https://smiskiworld.com/wp-content/uploads/2024/09/Smiski-World-Living-Series-Smiski-Nap-Time-1.webp"
    },
    {
        "smiski": "SMISKI LIFTING",
        "description": "You're the go-to Smiski for heavy lifting—whether it's weights, furniture, or the emotional baggage of\n"
            "your friends. Your strength isn't just physical; you're resilient, determined, and always ready to lend a\n"
            "hand (or two). But let's be honest, you look really cool doing it. Keep lifting, you powerhouse of\n"
            "positivity—you've got this!",
        "url": "https://smiskiworld.com/wp-content/uploads/2024/09/Smiski-World-Living-Series-Smiski-Lifting-1.webp"
    },
    {
        "smiski": "SMISKI THINKING",
        "description": "You're a deep thinker with a head full of ideas, questions, and maybe a conspiracy theory or two. Others\n"
           "might see you staring off into space, but you're busy solving the mysteries of the universe—or deciding\n"
            "what's for dinner. Your curiosity knows no bounds, and you're always finding creative solutions to life's\n"
            "little puzzles. Keep pondering, philosopher-in-residence.",
        "url": "https://i.postimg.cc/JnRPbWzn/image.png"
    },
    {
        "smiski": "SMISKI HIDING",
        "description": "You're the ultimate undercover operator, a cozy enigma wrapped in mystery. You prefer the quiet corners\n"
            "of the world, where you can observe, reflect, and occasionally snack in peace. People might not always\n"
            "notice you right away, but when they do, they discover a loyal and thoughtful companion who notices\n"
            "everything. Keep hiding—but don't be afraid to step into the spotlight every once in a while.",
        "url": "https://blinkbox.com.au/cdn/shop/files/smiski-series-1_hiding-looking-back.webp?crop=center&height=1500&v=1709333434&width=1500"
    },
    {
        "smiski": "RAINBOMB SMISKI",
        "description": "You're a burst of energy and surprises! One moment you're lost in thought, the next you're cracking jokes\n"
            "or planning spontaneous adventures. Your vibe is ever-changing, like a storm full of colorful chaos—and\n"
            "that's what makes you so fun to be around. Keep shining, you unpredictable Rainbomb!",
        "url": "https://www.japanla.com/cdn/shop/files/rainbombfloating.jpg?v=1699391153&width=320"
    }
]

def most_common(answer_list):
    #initializing counters
    a_counter = 0
    b_counter = 0
    c_counter = 0
    d_counter = 0

    #compiling data into list
    for x in answer_list:
        if x == "A":
            a_counter += 1
        elif x == "B":
            b_counter += 1
        elif x == "C":
            c_counter += 1
        elif x == "D":
            d_counter += 1

    counter_list = [a_counter, b_counter, c_counter, d_counter]
    most_common = max(counter_list)

    x = 0
    M = []
    m = most_common

    for i in counter_list:
        if i == m:
            M.append(x)
        x += 1

    if 0 in M and 3 in M:
        return "E"
    elif 0 in M and 2 in M:
        return "F"
    elif 0 in M:
        return "A"
    elif 1 in M:
        return "B"
    elif 2 in M:
        return "C"
    elif 3 in M:
        return "D"
    else:
        return "G"

@results_routes.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        # Collect answers from the form
        answers = request.form.to_dict()        
        answer_list = list(answers.values())

        # Find the most common answer
        mc = most_common(answer_list)
        answer_mapping = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
        
        if mc in answer_mapping:
            selected_result = smiski_results[answer_mapping[mc]]
        else:
            selected_result = smiski_results[6]

        return render_template("results.html", result=selected_result)
