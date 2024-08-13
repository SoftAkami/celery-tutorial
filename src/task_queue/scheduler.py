from celery.result import AsyncResult
from task_queue.celery_config import QueueName
from task_queue.tasks import counter
from task_queue.app import app


result: AsyncResult = counter.apply_async(
    (4,),
    shadow="my_job3",
    time_limit=200,  # Worker time limit
    queue=QueueName.QUEUE1
)

inspect = app.control.inspect()

result2: AsyncResult = counter.apply_async(
    (8,),
    shadow="my_job4",
    time_limit=200,  # Worker time limit
    queue=QueueName.QUEUE1
)

# Get active tasks
active_tasks = inspect.active()
print(active_tasks)

print(result.name)
print(result.task_id, result.queue)

print(result.ready())
print(result.state, result.status)

inspect = app.control.inspect()

# Get active tasks
active_tasks = inspect.active()
print(active_tasks)

print("info", app.AsyncResult(result.id).info)
print(result.get(timeout=200))
print(result2.get(timeout=200))
print(result)
print(result.ready())
print(result._get_task_meta())

