#!/usr/bin/env bash

echo "Start workers..."

celery --app task_queue.app worker --queues Queue1 --hostname=worker1@%h --concurrency=1 --loglevel=INFO &
celery --app task_queue.app worker --queues Queue1 --hostname=worker2@%h --concurrency=1 --loglevel=INFO &

# celery --app task_queue.app worker --queues Queue1 --hostname=worker1@%h --concurrency=1 --detach --loglevel=INFO --logfile /dev/tty1 2>&1 | tee output.log
# celery --app task_queue.app worker --queues Queue1 --hostname=worker2@%h --concurrency=1 --detach --loglevel=INFO --logfile /dev/tty1 2>&1 | tee output.log
# celery --app task_queue.app worker --queues Queue2 --hostname=worker3@%h --concurrency=1 --detach --loglevel=INFO --logfile /dev/tty1 2>&1 | tee output.log
# celery --app task_queue.app worker --queues Queue1,Queue2 --hostname=worker4@%h --concurrency=1 --detach --loglevel=INFO --logfile /dev/tty1 2>&1 | tee output.log