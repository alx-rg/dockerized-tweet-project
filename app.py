"""Main script, uses other modules to generate sentences."""
#git subtree push --prefix Code heroku master (from main folder/source)
from flask import Flask, redirect, request, render_template, render_template_string
from dictogram import Dictogram
from twitter import tweet

app = Flask(__name__)

@app.route("/")
def index():
    """Route that returns a web page containing the generated text."""
    return render_template('index.html')

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    print(status)
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
