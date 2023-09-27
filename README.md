# Dockerized Tweet Project

This is a Dockerized version of the Tweet Generator Flask application.
## Using docker-compose, run using the following commands:

Build the Docker Compose services:
`docker-compose build`

Run the Docker Compose services:
`docker-compose up`

These commands are used to build and start the Docker Compose services, as configured in the `docker-compose.yml` file.

If you only want to stop the containers for your project, in the project directory, run `docker-compose stop` or press Ctrl-C to stop a docker-compose process running in the foreground and then run `docker-compose stop` to ensure the project containers have stopped.

If you want to clean up project specific stopped containers, you can run: `docker-compose rm `from your project directory.
