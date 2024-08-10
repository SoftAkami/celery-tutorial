Celery existed for a long time

Can set time limit per task

Exchange
 - Direct Exchange: Use this when you want tasks to be routed to a queue with an exact match between the routing key and the queue name.
 - Topic Exchange: Use this when you need more flexible routing, such as routing tasks to multiple queues based on pattern matching in the routing key.
 - Fanout Exchange: Use this when you want to broadcast a task to multiple queues, regardless of routing keys.
 - Headers Exchange: Use this when you need advanced routing based on message headers.

Requirements
    Set task priority
    Send job to particular queue
    Able to see what is in queue
    Able to see what is in progress
    Able to find worker handling the task



Launch RabbitMQ server
```
sudo rabbitmq-server [-detached]
```

End RabbitMQ server
```
sudo rabbitmqctl stop
```

Start worker
```
# celery -A my_project worker -Q my_queue --hostname=my_worker@%h --loglevel=INFO
celery -A task_queue.celery_app worker -Q Queue1 --hostname=worker1@%h --concurrency=1 --loglevel=INFO
```

Active tasks
```
celery -A task_queue.app inspect active
```

```
rabbitmqctl list_queues --vhost dev_vhost
```

Purge message
```
celery -A task_queue.celery_app purge -Q Queue0
```

