from flask import Blueprint, request, render_template
from app.smiski_quiz import Image, display
from collections import Counter

results_routes = Blueprint("results_routes", __name__)

results = [
    {
        "smiski": "SMISKI DAYDREAMING",
        "description": "You're a whimsical wanderer, lost in the clouds but somehow always on time for dessert.\n"
            "Your imagination is your playground, and you're never short of quirky ideas or 'what if' scenarios.\n"
            "Whether it's pondering life's mysteries or deciding what the moon smells like, you're a creative soul who sees the world through a unique lens.\n"
            "Sure, you might forget where you put your keys (again), but you've probably already envisioned a secret portal hidden in the couch cushions anyway.\n"
            "Keep dreaming, you delightful daydreamer—you're proof that a little whimsy makes the world brighter!\n",
        "url": "https://preview.redd.it/secret-to-pulling-smiski-daydreaming-v0-7gnuu4h1qp8d1.jpeg?auto=webp&s=72d9d2fb0e27ea6cc97022316200ba13d4d184d2"
    },
    {
        "smiski": "SMISKI PLAYING",
        "description": "You're the life of the invisible party, a joyful creator who turns even the quietest moments into a celebration. \n"
           "Whether it's tapping out rhythms on a desk or choreographing secret dance moves in the kitchen, you find delight in simple pleasures. \n"
           "Others can't help but smile when they're around you—your energy is contagious! \n"
           "Keep playing your unique tune, you maestro of mischief.",
        "url": "https://media.karousell.com/media/photos/products/2024/9/12/smiski_living__playing_flute_1726152229_3bf7f0b5_progressive.jpg"
    },
    {
        "smiski": "SMISKI NAP TIME",
        "description": "You're a whimsical wanderer, lost in the clouds but somehow always on time for dessert.\n"
            "Your imagination is your playground,\n and you're never short of quirky ideas or 'what if' scenarios.\n"
            "Whether it's pondering life's mysteries or deciding what the moon smells like, you're a creative soul who sees the world through a unique lens.\n"
            "Sure, you might forget where you put your keys (again), but you've probably already envisioned a secret portal hidden in the couch cushions anyway.\n"
            "Keep dreaming, you delightful daydreamer—you're proof that a little whimsy makes the world brighter!\n",
        "url": "https://down-my.img.susercontent.com/file/3b89d452f033e9251f289a976228d56b"
    },
    {
        "smiski": "SMISKI LIFTING",
        "description": "You're a whimsical wanderer, lost in the clouds but somehow always on time for dessert.\n"
            "Your imagination is your playground,\n and you're never short of quirky ideas or 'what if' scenarios.\n"
            "Whether it's pondering life's mysteries or deciding what the moon smells like, you're a creative soul who sees the world through a unique lens.\n"
            "Sure, you might forget where you put your keys (again), but you've probably already envisioned a secret portal hidden in the couch cushions anyway.\n"
            "Keep dreaming, you delightful daydreamer—you're proof that a little whimsy makes the world brighter!\n",
        "url": "https://www.publicisdrugstore.com/17949-square_large_default/smiski-living-room.jpg"
    },
    {
        "smiski": "SMISKI THINKING",
        "description": "You're a whimsical wanderer, lost in the clouds but somehow always on time for dessert.\n"
            "Your imagination is your playground,\n and you're never short of quirky ideas or 'what if' scenarios.\n"
            "Whether it's pondering life's mysteries or deciding what the moon smells like, you're a creative soul who sees the world through a unique lens.\n"
            "Sure, you might forget where you put your keys (again), but you've probably already envisioned a secret portal hidden in the couch cushions anyway.\n"
            "Keep dreaming, you delightful daydreamer—you're proof that a little whimsy makes the world brighter!\n",
        "url": "https://media.karousell.com/media/photos/products/2024/5/24/smiski_thinking_1716567214_22088f5b_progressive"
    },
    {
        "smiski": "SMISKI HIDING",
        "description": "You're a whimsical wanderer, lost in the clouds but somehow always on time for dessert.\n"
            "Your imagination is your playground,\n and you're never short of quirky ideas or 'what if' scenarios.\n"
            "Whether it's pondering life's mysteries or deciding what the moon smells like, you're a creative soul who sees the world through a unique lens.\n"
            "Sure, you might forget where you put your keys (again), but you've probably already envisioned a secret portal hidden in the couch cushions anyway.\n"
            "Keep dreaming, you delightful daydreamer—you're proof that a little whimsy makes the world brighter!\n",
        "url": "https://media.karousell.com/media/photos/products/2024/11/5/smiski_living_series__hiding_1730796363_ade886ef_progressive.jpg"
    },
    {
        "smiski": "RAINBOMB SMISKI",
        "description": "You're a whimsical wanderer, lost in the clouds but somehow always on time for dessert.\n"
            "Your imagination is your playground, and you've never short of quirky ideas or 'what if' scenarios.\n"
            "Whether it's pondering life's mysteries or deciding what the moon smells like, you're a creative soul who sees the world through a unique lens.\n"
            "Sure, you might forget where you put your keys (again), but you've probably already envisioned a secret portal hidden in the couch cushions anyway.\n"
            "Keep dreaming, you delightful daydreamer—you're proof that a little whimsy makes the world brighter!\n",
        "url": "https://www.japanla.com/cdn/shop/files/rainbombfloating.jpg?v=1699391153&width=320"
    }
]

def most_common(answer_list):
    # Counter returns a dictionary-like object with answer counts
    counts = Counter(answer_list)
    # Return the most common answer (the one with the highest count)
    return counts.most_common(1)[0][0]

# @results_routes.route('/results', methods=["POST"])
# def quiz():
#     if request.method == 'POST':
#         # Get answers from form
#         answer_list = request.form.getlist('answer')
        
#         # Calculate result based on answers
#         result = calculate_result(answer_list)
        
#         return render_template('result.html', result=result)
    
#     return render_template('quiz.html')

@results_routes.route("/results", methods=["POST"])
def results():
    # Collect answers from the form
    answers = request.form.to_dict()
    answer_list = list(answers.values())  # Extract all answers into a list

    # Find the most common answer
    mc = most_common(answer_list)

    # Map the answer to the corresponding result
    answer_mapping = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
    
    # Check if the most common answer exists in the answer_mapping
    if mc in answer_mapping:
        selected_result = results[answer_mapping[mc]]
    else:
        # Handle case where answer is not found in the mapping
        selected_result = results[0]  # Default to the first result (or handle as needed)

    # Render the result template with the selected result
    return render_template("results.html", result=selected_result)