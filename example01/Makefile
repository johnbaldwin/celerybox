.PHONY: help start.worker
# Make sure you create the .env file with the variables specified in the `.env.template` file

makefile_name := $(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))

# include .env

help:  ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@grep '^[a-zA-Z]' $(makefile_name) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'


start.worker:  ## Start the worker
	# This runs the worker on the host
	@celery -A example01_app worker -l INFO
