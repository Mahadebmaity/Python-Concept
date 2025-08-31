from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# Sentence parts
subjects = [
    "A giant chicken", "Aliens", "A time traveler", "A robot from the future",
    "An invisible man", "A billionaire dog", "A haunted pizza"
]
verbs = [
    "attacks", "discovers", "destroys", "hacks", "saves", "tricks", "clone"
]
objects = [
    "the White House", "the Moon", "an entire country", "a secret lab",
    "a lost island", "NASA", "a famous celebrity"
]
reasons = [
    "to gain superpowers", "to stop global warming", "for revenge",
    "to start a new civilization", "to impress their crush", "for YouTube views"
]

# File to store generated headlines
HEADLINE_FILE = "generated_headlines.txt"

# Generate one fake news line
def generate_fake_news():
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)} {random.choice(reasons)}!"

# Save headlines to file
def save_headlines_to_file(headlines):
    with open(HEADLINE_FILE, "a", encoding="utf-8") as f:
        for headline in headlines:
            f.write(headline + "\n")

@app.route('/')
def home():
    headlines = [generate_fake_news() for _ in range(1)]
    save_headlines_to_file(headlines)
    return render_template('index.html', headlines=headlines)

if __name__ == '__main__':
    # Create file if not exists
    if not os.path.exists(HEADLINE_FILE):
        open(HEADLINE_FILE, "w", encoding="utf-8").close()

    app.run(debug=True)
