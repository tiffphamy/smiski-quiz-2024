from IPython.display import Image, display
from operator import itemgetter

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
        "options": "a) Dreamy—you’re always off in your own little world.\nb) Playful—you bring energy and joy wherever you go.\nc) Relaxed—you’re a chill presence who loves to recharge.\nd) Strong—you’re dependable, resilient, and there when it counts."
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

#storing data in dictionary to find max
counters = {
    "A": a_counter,
    "B": b_counter,
    "C": c_counter,
    "D": d_counter
}

#results logic
if counters["A"] > 3:
    print("You are: SMISKI DAYDREAMING!")
    print("You're a whimsical wanderer, lost in the clouds but somehow always on time for dessert. Your imagination is your playground, \n"
          "and you’re never short of quirky ideas or 'what if' scenarios. Whether it's pondering life’s mysteries or deciding what the moon smells like, \n"
          "you're a creative soul who sees the world through a unique lens. Sure, you might forget where you put your keys (again), but you’ve probably already \n"
          "envisioned a secret portal hidden in the couch cushions anyway. Keep dreaming, you delightful daydreamer—you’re proof that a little whimsy makes the world brighter!")
    display(Image(url="https://preview.redd.it/secret-to-pulling-smiski-daydreaming-v0-7gnuu4h1qp8d1.jpeg?auto=webp&s=72d9d2fb0e27ea6cc97022316200ba13d4d184d2", height = 300))
elif counters["B"] >= 3:
    print("You are: SMISKI PLAYING!")
    print("You’re the life of the invisible party, a joyful creator who turns even the quietest moments into a celebration. \n"
          "Whether it's tapping out rhythms on a desk or choreographing secret dance moves in the kitchen, you find delight in simple pleasures. \n"
          "Others can’t help but smile when they’re around you—your energy is contagious! \n"
          "Keep playing your unique tune, you maestro of mischief.")
    display(Image(url="https://media.karousell.com/media/photos/products/2024/9/12/smiski_living__playing_flute_1726152229_3bf7f0b5_progressive.jpg", height = 300))
elif counters["C"] > 3:
    print("You are: SMISKI NAP TIME!")
    print("A true champion of rest and relaxation, you’ve mastered the art of doing nothing—and doing it well.\n"
          "Whether it’s a 10-minute snooze or a full-blown nap marathon, \n"
          "you know that recharging is the secret to your brilliance. Some might call you “lazy,” but you call it “energy management.”\n"
          "Dream big, nap often, and keep being unapologetically chill.")
    display(Image(url="https://down-my.img.susercontent.com/file/3b89d452f033e9251f289a976228d56b", height = 300))
elif counters["D"] > 3:
    print("You are: SMISKI LIFTING!")
    print("You’re the go-to Smiski for heavy lifting—whether it’s weights, furniture, or the emotional baggage of your friends.\n"
          "Your strength isn’t just physical; you’re resilient, \n"
          "determined, and always ready to lend a hand (or two). But let’s be honest, you look really cool doing it.\n"
          "Keep lifting, you powerhouse of positivity—you’ve got this!")
    display(Image(url="https://www.publicisdrugstore.com/17949-square_large_default/smiski-living-room.jpg", height = 300))
elif counters["A"] == 3 and counters["D"] == 3:
    print("You are: SMISKI THINKING!")
    print("You’re a deep thinker with a head full of ideas, questions, and maybe a conspiracy theory or two.\n"
          "Others might see you staring off into space, but you’re busy solving the mysteries \n"
          "of the universe—or deciding what’s for dinner. Your curiosity knows no bounds, and you’re always finding creative solutions to life’s little puzzles.\n"
          "Keep pondering, philosopher-in-residence.")
    display(Image(url="https://media.karousell.com/media/photos/products/2024/5/24/smiski_thinking_1716567214_22088f5b_progressive", height = 300))
elif counters["A"] == 3 and counters["C"] == 3:
    print("You are: SMISKI HIDING!")
    print("You’re the ultimate undercover operator, a cozy enigma wrapped in mystery.\n"
          "You prefer the quiet corners of the world, where you can observe, reflect, and occasionally snack in peace.\n"
          "People might not always notice you right away, but when they do, they discover a loyal and thoughtful companion who notices everything.\n"
          "Keep hiding—but don’t be afraid to step into the spotlight every once in a while.")
    display(Image(url="https://media.karousell.com/media/photos/products/2024/11/5/smiski_living_series__hiding_1730796363_ade886ef_progressive.jpg", height = 300))
else:
    print("You are: RAINBOM SMISKI!")
    print("You’re a burst of energy and surprises! One moment you’re lost in thought, the next you’re cracking jokes or planning spontaneous adventures.\n"
        "Your vibe is ever-changing, like a storm full of colorful chaos—and that’s what makes you so fun to be around. \n"
        "Keep shining, you unpredictable Rainbomb!")
    display(Image(url="https://www.japanla.com/cdn/shop/files/rainbombfloating.jpg?v=1699391153&width=320", height = 300))