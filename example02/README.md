# Celerybox Example 2 - Celery worker in a container

## Overview

This example builds on [example 1](../example01).

* We now run the Celery worker in a Docker container
* RabbitMQ runs in a container, like example 1, except now both the RabbitMQ server and the Celery worker are launched together in the same Docker Compose file

## Requirements

* Python 3.7+
* Docker and Docker Compose installed
* Internet connection

## Get it running

For the example, you'll need two shells (consoles) open
* One to start the containers with Docker Compose
* One for the Celery client app

### Step 1 - Run Docker Compose

This starts the RabbitMQ and Celery worker containers in attached mode.

* Open a shell
* Navigate to the `celerybox/example02` directory
* Run `make up`

### Step 2 - Run the app

* Open a shell
* Navigate to the `celerybox/example02` directory
* Create/enable your virtualenv
* Run `pip install -r requirements.txt` (if you haven't already done this)
* Run `python simple_client.py`
* Watch the output in the Docker Compose

## After that

Check out the code.

This example uses the admin account credentials assigned to the RabbitMQ server when Docker created the RabbitMQ container. You'll see the `BROKER_URL` value that has the username and password hardcoded into the `BROKER_URL` connect string in `example02_app/celery.py`
