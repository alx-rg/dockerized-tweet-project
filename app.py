"""Main script, uses other modules to generate sentences."""
#git subtree push --prefix Code heroku master (from main folder/source)
from flask import Flask, redirect, request, render_template
import twitter
from markov import markov_chain, create_sentence
from tokens import get_token
from tasks import get_open_and_lower

app = Flask(__name__)

open_text_file = get_open_and_lower('words-sample.txt')
tokenized_text_file = get_token(open_text_file)
markov = markov_chain(tokenized_text_file)

@app.route("/")
def index():
    sentence = create_sentence(markov, 80)
    """Route that returns a web page containing the generated text."""
    return render_template('index.html', sentence=sentence)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    # print(status)
    return redirect('/')

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)


# Things to remember:
# python3 -m venv env
# source venv/bin/activate
# If you ever want to deactivate your virtual environment, just type deactivate in your terminal window.#
# export FLASK_ENV=development; flask run
# http://127.0.0.1:5000/
# localhost:5000
