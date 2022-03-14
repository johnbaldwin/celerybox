#!/bin/sh
#
# Run this script from within the RabbitMQ docker container


rabbitmqctl add_user bunnydemo_user setec-astronomy
rabbitmqctl add_vhost bunnydemo_vhost
rabbitmqctl set_user_tags bunnydemo_user bunnydemo_tag
rabbitmqctl set_permissions -p bunnydemo_vhost bunnydemo_user ".*" ".*" ".*"

