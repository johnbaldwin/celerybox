
.PHONY: help
# Make sure you create the .env file with the variables specified in the `.env.template` file

makefile_name := $(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))

# include .env

help:  ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@grep '^[a-zA-Z]' $(makefile_name) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

basic.up:  ## Start the basic RabbitMQ server
	@docker-compose -f docker-compose-basic.yml up

basic.up.detach:  ## Start the basic RabbitMQ server in detached mode
	@docker-compose -f docker-compose-basic.yml up --detached

basic.up.down:  ## Stop the basic RabbitMQ server (Use when started in detach mode)
	@docker-compose -f docker-compose-basic.yml down

basic.rm:  ## Remove the basic RabbitMQ server container
	@docker-compose -f docker-compose-basic.yml rm

basic.ssh:  ## SSH to the basic RabbitMQ server container
	@docker exec -it basic-rabbitmq /bin/bash

basic.configure-bunnydemo:  ## Configures the 'bunnydemo' environment on the basic RabbitMQ container
	@docker exec -it /workspace/rabbitmq-configure-bunnydemo.sh

basic.logs:  ## Show logs on the RabbitMQ docker container
	@docker container logs basic-rabbitmq
