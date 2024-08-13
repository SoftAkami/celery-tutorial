import logging
import os
import sys
import time

from celery.utils.log import get_task_logger
from celery.app.log import get_current_task
from celery import Task

from task_queue.app import app
from my_project.config import PROJECT_ROOT
from my_project.counter import custom_counter
from utils.logging_tool import CUSTOM_TIME_FORMAT

# Celery will overwite sys.stdout and sys.stderr with `LoggingProxy`.
# Keep a copy of original.
STDOUT = sys.stdout
STDERR = sys.stderr


task_logger = get_task_logger(__name__)


class TimePathTaskFormatter(logging.Formatter):
    """
    Custom logger for Celery tasks.
    """
    custom_time_format = CUSTOM_TIME_FORMAT

    def __init__(
        self,
        fmt=None,
        datefmt=None,
        style='%',
        validate=True,
        *,
        defaults=None,
        project_root=None,
    ):
        self.project_root = project_root
        super().__init__(
            fmt, datefmt, style, validate, defaults=defaults
        )

    def format(self, record):

        # Copied from `celery.app.log.TaskFormatter.format()` and modified
        task: Task = get_current_task()
        if task and task.request:
            record.__dict__.update(
                hostname=task.request.hostname,
                task_name=task.name,
                task_shadow_name=task.request.shadow,
                task_id=task.request.id
            )
        else:
            record.__dict__.setdefault('hostname', '???')
            record.__dict__.setdefault('task_name', '???')
            record.__dict__.setdefault('task_shadow_name', '???')
            record.__dict__.setdefault('task_id', '???')

        # Get the module's path
        module_path = os.path.dirname(os.path.abspath(record.pathname))
        # Convert it to a path relative to the project root
        relative_path = os.path.relpath(module_path, self.project_root)
        # Include the relative path in the log message
        record.relative_path = relative_path.replace("/", ".") + "." + record.module
        return super().format(record)

    def formatTime(self, record, datefmt=None):
        """
        Overwrite `formatTime` to insert `msecs` before timezone offset.
        """
        if datefmt == self.custom_time_format:

            ct = self.converter(record.created)
            s = time.strftime(self.custom_time_format, ct) % {
                'msecs': int(record.msecs)
            }
            return s

        return super().formatTime(record, datefmt)


formatter = TimePathTaskFormatter(
    fmt=(
        ">1|%(levelname)-5s|%(asctime)s|%(relative_path)s|%(module)s:%(lineno)d|"
        "[%(hostname)s:%(processName)s(%(process)d)][%(threadName)s(%(thread)d)]"
        "[%(task_shadow_name)s:%(task_name)s(%(task_id)s)]"
        "%(name)s - %(message)s"
    ),
    datefmt=CUSTOM_TIME_FORMAT,
    project_root=PROJECT_ROOT
)


stream_handler = logging.StreamHandler(STDOUT)
stream_handler.setFormatter(formatter)

proj_logger = logging.getLogger("my_project")
proj_logger.setLevel(logging.DEBUG)
proj_logger.addHandler(stream_handler)
proj_logger.propagate = False


@app.task(bind=True, track_started=True)
def counter(self: Task, t: int):

    self.update_state(meta={"test": 1})
    task_logger.info("My test task logger")
    print(self.request)
    return custom_counter(t)