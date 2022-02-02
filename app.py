"""Main script, uses other modules to generate sentences."""
from flask import Flask
#from histogram import histogram

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    #histo = histogram()
    #return histo
    # TODO: Initialize your histogram, hash table, or markov chain here.


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    return f"<p>Random Word from Space.. Return a word here!</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
