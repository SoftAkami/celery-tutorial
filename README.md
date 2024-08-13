Requirements
 - Set task priority
 - Send job to particular queue
 - Able to see what is in queue
 - Able to see what is in progress
 - Able to find worker handling the task

## Celery
 - Celery is a distributed task queue library written in Python.
 - Support automatic retry.
 - Support prefork for multiprocessing
 - Task time limit.
 - Doesn't support Windows.

Additional features
 - Scheduling.
 - Native Flask web framework

Can set time limit per task

Exchange
 - Direct Exchange: Use this when you want tasks to be routed to a queue with an exact match between the routing key and the queue name.
 - Topic Exchange: Use this when you need more flexible routing, such as routing tasks to multiple queues based on pattern matching in the routing key.
 - Fanout Exchange: Use this when you want to broadcast a task to multiple queues, regardless of routing keys.
 - Headers Exchange: Use this when you need advanced routing based on message headers.

### Logging
 - Predefined logger
    - 'celery'
    - 'celery.task'
    - 'celery.redirect'
        `print()` to `stdout` and `stderr` will be shown under `logging.WARNING`.
 - Root logger uses worker_log_format




## Setup
 - Standalone RabbitMQ service. See Dockerfile.rabbitmq.


Start worker
```
# celery -A my_project worker -Q my_queue -n=my_worker@%h -c=1 -l=INFO
celery -A task_queue.app worker -Q Queue1 -n=worker1@%h  -c=1 -l=INFO
```

List queues consumed by each worker
```
celery -A task_queue.app inspect active_queues
```

Inpect active tasks of each worker
```
celery -A task_queue.app inspect active
```

Purge message
```
celery -A task_queue.app purge -Q Queue0
```

Shutdown workers
```
celery -A task_queue.app control shutdown
```

Celery redirects stdout (where print writes its output) to the logger at the WARNING level by default

## RabbitMQ
Diagnostics in RabbitMQ
```
rabbitmqctl list_queues --vhost dev_vhost
```

Launch RabbitMQ server
```
sudo rabbitmq-server -detached
```

End RabbitMQ server
```
sudo rabbitmqctl stop
```

