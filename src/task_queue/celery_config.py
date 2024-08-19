from enum import Enum, unique
from kombu import Queue


WORKER_LOG_FORMAT = (
    "[%(levelname)-5s|%(asctime)s|%(processName)s]%(name)s - %(message)s"
)
WORKER_TASK_LOG_FORMAT = (
    "[%(levelname)-5s|%(asctime)s|%(processName)s]"
    "[%(task_name)s|%(task_id)s]%(name)s - %(message)s"
)


@unique
class QueueName(str, Enum):

    QUEUE0 = "Queue0"
    QUEUE1 = "Queue1"
    QUEUE2 = "Queue2"


class Config:

    # result_expires = 10
    result_extended = True

    task_default_exchange = 'task_exchange'
    task_default_exchange_type = 'direct'
    task_default_routing_key = 'task.default'

    task_queues=(
        Queue(QueueName.QUEUE0, routing_key='queue0.#'),
        Queue(QueueName.QUEUE1, routing_key='queue1.#'),
        Queue(QueueName.QUEUE2, routing_key='queue2.#'),
    )
    task_default_queue = QueueName.QUEUE0  # Default queue used by `task.apply_async`

    # Wipe existing handlers from root logger.
    # See https://github.com/celery/celery/blob/a1878911ec2ea0accccdfad547b4b74c7ec1c3df/celery/app/log.py#L105
    worker_hijack_root_logger = False
    
    worker_log_format = WORKER_LOG_FORMAT
    worker_task_log_format = WORKER_TASK_LOG_FORMAT
    # worker_redirect_stdouts = False

    # Setting task_ack_late = False and worker_prefetch_multiplier = 1
    # will reserve 1 task in addition to 1 task in progress per worker.
    # See https://docs.celeryq.dev/en/stable/userguide/optimizing.html#reserve-one-task-at-a-time
    task_acks_late = True
    worker_prefetch_multiplier = 1  # Disable prefetching
