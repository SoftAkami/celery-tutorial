#!/usr/bin/env bash

echo "Start workers..."
celery --app task_queue.app worker --queues Queue1 --hostname=worker1@%h --concurrency=1 --detach --loglevel=INFO
celery --app task_queue.app worker --queues Queue1 --hostname=worker2@%h --concurrency=1 --detach --loglevel=INFO
celery --app task_queue.app worker --queues Queue2 --hostname=worker3@%h --concurrency=1 --detach --loglevel=INFO
celery --app task_queue.app worker --queues Queue1,Queue2 --hostname=worker4@%h --concurrency=1 --detach --loglevel=INFO