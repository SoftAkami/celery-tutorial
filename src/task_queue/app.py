from celery import Celery
from kombu import Queue

from task_queue.config import QueueName


app = Celery(
    'my_task_queue',
    broker='amqp://dev:dev_pw@rabbitmq:5672/dev_vhost',
    backend='rpc://',
    include=['task_queue.worker']
)

app.conf.update(
    result_expires=10,  # Remove RabbitMQ backend result temp queue
    
    result_extended=True,

    task_default_exchange='tasks',
    task_default_exchange_type='direct',
    task_default_routing_key='task.default',

    task_queues=(
        Queue(QueueName.QUEUE0, routing_key='queue0.#'),
        Queue(QueueName.QUEUE1, routing_key='queue1.#'),
    ),
    task_default_queue=QueueName.QUEUE0  # Default queue used by `task.apply_async`
)

if __name__ == '__main__':
    app.start()
