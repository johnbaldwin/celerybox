# Celerybox Example 1 - Simple app

## Overview

This directory provides an introductory example to use Celery with RabbitMQ

* Start a RabbitMQ server with Docker Compose using an official image
* Configure the RabbitMQ server for the example project
* Explore the RabbitMQ interface

## Requirements

* Python 3.7+
* Docker and Docker Compose installed
* Internet connection

## Get it running

For the example, you'll need three shells (consoles) open
* One for the RabbitMQ server
* One for the Celery worker
* One for your app to call the Celery worker

The purpose of having these three shells open is to see what's going on.

### Step 1 - Start the RabbitMQ server

* Open a shell and navigate to the `celerybox/rabbitmq` directory
* Run `make basic.up` to start the RabbitMQ server (not detached mode)

### Step 2 - Start the Celery worker

* Open a shell
* Navigate to the `celerybox/example01` directory
* Create your virtualenv
* Enable your virtualenv
* Run `pip install -r requirements.txt`
* Run `make start.worker` to start the Celery worker

### Step 3 - Run the app

* Open a shell
* Navigate to the `celerybox/example01` directory
* Enable your virtualenv (what you created in step 2)
* Run `python my_app.py`
* Watch the output

## After that

Check out the code.

This example uses the admin account credentials assigned to the RabbitMQ server when Docker created the RabbitMQ container. You'll see the `BROKER_URL` value that has the username and password hardcoded into the `BROKER_URL` connect string.
