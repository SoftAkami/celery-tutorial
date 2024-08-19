from celery.result import AsyncResult
from celery import group

from task_queue.celery_config import QueueName
from task_queue.tasks import counter
from task_queue.app import app

import time

res = (
    counter.signature(
        args=(3,),
        options={
            "shadow": "my_job1",
            "time_limit": 200,
            "queue": QueueName.QUEUE1
        },
        immutable=True
    ) |
    group(
        counter.signature(
            args=(4,),
            options={
                "shadow": "my_job2",
                "time_limit": 200,
                "queue": QueueName.QUEUE1
            },
            immutable=True
        ),
        counter.signature(
            args=(4,),
            options={
                "shadow": "my_job3",
                "time_limit": 200,
                "queue": QueueName.QUEUE2
            },
            immutable=True
        ),
        counter.signature(
            args=(4,),
            options={
                "shadow": "my_job4",
                "time_limit": 200,
                "queue": QueueName.QUEUE1
            },
            immutable=True
        ),
        counter.signature(
            args=(4,),
            options={
                "shadow": "my_job5",
                "time_limit": 200,
                "queue": QueueName.QUEUE1
            },
            immutable=True
        )
        ,
        counter.signature(
            args=(4,),
            options={
                "shadow": "my_job6",
                "time_limit": 200,
                "queue": QueueName.QUEUE1
            },
            immutable=True
        ),
        counter.signature(
            args=(4,),
            options={
                "shadow": "my_job7",
                "time_limit": 200,
                "queue": QueueName.QUEUE1
            },
            immutable=True
        ),
        counter.signature(
            args=(4,),
            options={
                "shadow": "my_job8",
                "time_limit": 200,
                "queue": QueueName.QUEUE1
            },
            immutable=True
        ),
        counter.signature(
            args=(4,),
            options={
                "shadow": "my_job9",
                "time_limit": 200,
                "queue": QueueName.QUEUE1
            },
            immutable=True
        ),
        counter.signature(
            args=(4,),
            options={
                "shadow": "my_job10",
                "time_limit": 200,
                "queue": QueueName.QUEUE1
            },
            immutable=True
        )
    )
)()
print(res)
print(res.get(timeout=200))
