from celery.result import AsyncResult
from task_queue.celery_config import QueueName
from task_queue.tasks import counter
from task_queue.app import app

import time


result: AsyncResult = counter.apply_async(
    (3,),
    shadow="my_job1",
    time_limit=200,  # Worker time limit
    queue=QueueName.QUEUE1
)
result2: AsyncResult = counter.apply_async(
    (4,),
    shadow="my_job2",
    time_limit=200,  # Worker time limit
    queue=QueueName.QUEUE1,
)

inspect = app.control.inspect()
print(inspect.active())

time.sleep(5)

result3: AsyncResult = counter.apply_async(
    (5,),
    shadow="my_job3",
    time_limit=200,  # Worker time limit
    queue=QueueName.QUEUE1
)
print(1)
print(result.state, result2.state, result3.state)


# Get active tasks
print(inspect.active())

print(app.AsyncResult(result.id)._get_task_meta())
print(app.AsyncResult(result2.id)._get_task_meta())
print(app.AsyncResult(result3.id)._get_task_meta())

print(1)
print(result.get(timeout=200))
print(2)
print(result2.get(timeout=200))

print(app.AsyncResult(result.id)._get_task_meta())
print(app.AsyncResult(result2.id)._get_task_meta())
print(app.AsyncResult(result3.id)._get_task_meta())

# Calls `celery.backends.rpc.get_task_meta`
print(result._get_task_meta())
