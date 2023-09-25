# Dockerized Tweet Project

This is a Dockerized version of the Tweet Generator Flask application.

## Prerequisites

Before you begin, ensure you have the following requirements:

- Docker installed on your system.

## Getting Started

Follow these instructions to build and run the Docker container for your Flask application:

1. Clone the repository:

  ```bash
  git clone https://github.com/alx-rg/dockerized-tweet-project.git
  ```

2. Navigate to the project directory:

  ```
  cd dockerized-tweet-project
  ```

3. Build the Docker image:

  ```
  docker build -t dockerized-tweet-project .
  ```

4. Run the Docker container:

  ```
  docker run -p 3000:3000 --rm --name tweet-container dockerized-tweet-project
  ```

5. Access in Browser

http://localhost:3000

The Flask application should now be accessible in your browser.

<!-- Things to note if you don't want to use Docker and just run it in your virtual env:

Make sure you're in the project directory

Create and activate a virtual environment
- `python3 -m venv env`
- `source venv/bin/activate`

To check that you are in your virtual environment type in: `which python`
If you get something along the lines of `/path/to/your/virtualenv/bin/python` then your virtual environment is properly set up.

Once you're in your virtual environment, install the required dependencies from requirements.txt:
`pip install -r requirements.txt`


Set the Flask environment variable and run the Flask app:
 `export FLASK_ENV=development; flask run`
Access the website @ `http://127.0.0.1:5000/`
`localhost:5000`

If you ever want to deactivate your virtual environment, just type `deactivate` in your terminal window. -->
