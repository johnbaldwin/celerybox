# Celerybox

This repo is a simple [Celery](https://docs.celeryproject.org/) sandbox environment. I started it because I wanted to be able to test Celery functionality and parts of the Celery ecosystem in an environment that would make it cheap and easy to stand up, explore, tear down, and evolve.

## What you'll need

* Python 3.7+ environment, virtualenv, pip
    * If you're not familiar with [pyenv](https://github.com/pyenv/pyenv), give it a try to manage your Python versions and virtual environments
* Docker (I'm using version 20)
* Docker Compose
* Make
* Linux. Probably will also work on OS X, WSL, BSD
* Maybe something else I forgot about

## What's here now?

* [rabbitmq](./rabbitmq) - RabbitMQ Docker Compose set-up
* [example01](./example01) - Basic Celery example to run a worker and a app to run tasks
