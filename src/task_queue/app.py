from celery import Celery

from task_queue.celery_config import Config

from celery import signals


@signals.celeryd_init.connect
def setup_log_format(sender, conf, **kwargs):
    conf.worker_log_format = (
        "|%(levelname)s|%(asctime)s|"
        "[{0}:%(processName)s(%(process)d)]"
        "%(name)s- %(message)s"
    ).format(sender)
    conf.worker_task_log_format = (
        "|%(levelname)s|%(asctime)s|"
        "[{0}:%(processName)s(%(process)d)][%(task_name)s(%(task_id)s)]"
        "%(name)s- %(message)s"
    ).format(sender)


app = Celery(
    'my_task_queue',
    broker="amqp://dev:dev_pw@rabbitmq:5672/dev_vhost",
    backend="rpc://",
    include=['task_queue.tasks']
)
app.config_from_object(Config)

if __name__ == '__main__':
    app.start()
