# Celerybox - RabbitMQ

This directory contains files to run RabbitMQ in a Docker container.

The `Makefile` in this directory provides convenience targets for basic actions.

Run `make` (or `make help`. the `help` target is the default target) to show the targets you can run.

## RabbitMQ Web UI

After you start the RabbitMQ server, navigate to here: [http://localhost:15672](http://localhost:15672/) for the web UI. Use "admin" and "admin" for the username and password. Of course, this is for local development only. Never do this for production.
