from IPython.display import Image, display
from operator import itemgetter
from collections import Counter

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
    
def results(answer_list, smiski_results):
    mc = most_common(answer_list)
    answer_mapping = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
    if mc in answer_mapping:
        selected_result = smiski_results[answer_mapping[mc]]
    else:
        selected_result = smiski_results[6]
    return selected_result

if __name__ == "__main__":
    #setting up environment
    answer_list = []
    a_counter = 0
    b_counter = 0
    c_counter = 0
    d_counter = 0

    ##QUIZ
    #questions list
    questions = [
        {
            "question": "Question 1: How do you like to spend your free time?",
            "options": "a) Imagining wild scenarios and daydreaming about 'what could be.'\nb) Dancing, singing, or just finding ways to add a little fun to the moment.\nc) Curling up somewhere cozy for a much-needed nap.\nd) Thinking through big ideas and solving life's little mysteries."
        },
        {
            "question": "Question 2: What is your go-to vibe in a group setting?",
            "options": "a) Quietly observing from the sidelines—you like to keep things low-key.\nb) Jumping in to entertain and make everyone smile—you’re the fun one!\nc) Offering thoughtful advice or coming up with a genius plan.\nd) Helping wherever you’re needed—lifting the mood or literal furniture!"
        },
        {
            "question": "Question 3: If your friends described you in one word, what would it be?",
            "options": "a) Dreamy—you're always off in your own little world.\nb) Playful—you bring energy and joy wherever you go.\nc) Relaxed—you’re a chill presence who loves to recharge.\nd) Strong—you’re dependable, resilient, and there when it counts."
        },
        {
            "question": "Question 4: What’s your ideal environment?",
            "options": "a) A cozy corner where you can quietly reflect or observe.\nb) A lively space with lots of energy and good vibes.\nc) Anywhere with soft blankets and a place to snooze.\nd) Somewhere you can think, create, or tackle challenges."
        },
        {
        "question": "Question 5: How do you usually approach a problem?",
        "options": "a) By brainstorming creative solutions and imagining the possibilities.\nb) By jumping in with enthusiasm and keeping it upbeat.\nc) By staying calm, assessing the situation, and taking your time.\nd) By tackling it head-on with focus and determination."
        },
        {
        "question": "Question 6: What’s your ultimate self-care routine?",
        "options": "a) Letting your mind wander with a good book or journaling.\nb) Doing something fun like dancing or catching up with friends.\nc) Relaxing in your favorite spot with cozy vibes all around.\nd) Engaging in a project or hobby that recharges your energy."
        },
        {
        "question": "Question 7: What type of adventure appeals to you most?",
        "options": "a) A quiet retreat where you can explore new ideas and reflect.\nb) A lively road trip with spontaneous stops and laughter.\nc) A laid-back beach day with no plans but to unwind.\nd) An active challenge"
        }
    ]

    #output quiz
    for x in questions:
        print(x["question"])
        print(x["options"])
        while True:
            answer = input("Enter your choice (a/b/c/d): ").upper()
            print("---------------------")
            if answer in ["A", "B", "C", "D"]:
                answer_list.append(answer)
                break
            else:
                print("Invalid input. Enter your choice (a/b/c/d):")

    #adding space for reading clarity
    print("---------------------")
    selected_result = results(answer_list, smiski_results)
    print(selected_result["smiski"])
    print(selected_result["description"])
