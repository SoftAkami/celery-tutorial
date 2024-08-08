#!/usr/bin/env bash

# Start RabbitMQ server in the background
echo "Starting RabbitMQ server..."
rabbitmq-server -detached

# Wait for RabbitMQ to be fully up and running
echo "Waiting for RabbitMQ to start..."
until rabbitmqctl status > /dev/null 2>&1; do
  sleep 1
done

rabbitmqctl add_user dev dev_pw
rabbitmqctl add_vhost dev_vhost
rabbitmqctl set_user_tags dev dev_tag
rabbitmqctl set_permissions -p dev_vhost dev ".*" ".*" ".*"