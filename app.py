"""Main script, uses other modules to generate sentences."""
from flask import Flask
from dictogram import Dictogram

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    histogram = Dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
    return histogram
    # TODO: Initialize your histogram, hash table, or markov chain here.


@app.route("/")
def home():
    calling_histogram = before_first_request()
    random_word = calling_histogram
    """Route that returns a web page containing the generated text."""
    return f"Random Word from fishes: {random_word}"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
