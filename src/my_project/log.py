import logging
import sys

from utils.logging_tool import TimePathFormatter, CUSTOM_TIME_FORMAT
from my_project.config import PROJECT_ROOT


LOGGER_FORMAT = (
    ">1|%(levelname)-5s|%(asctime)s|%(relative_path)s|%(module)s:%(lineno)d|"
    "%(name)s - %(message)s"
)
fmt = logging.Formatter(
    fmt=(
        ">1|%(levelname)-5s|%(asctime)s|%(pathname)s|%(module)s:%(lineno)d|"
        "[%(processName)s(%(process)d)][%(threadName)s(%(thread)d)][%(taskName)s]"
        "%(name)s - %(message)s"
    )
)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(fmt)

logging.basicConfig(
    level=logging.INFO,
    handlers=[stream_handler]
)

formatter = TimePathFormatter(
    fmt=">1|%(levelname)-5s|%(asctime)s|%(pathname)s|%(module)s:%(lineno)d|%(name)s|%(processName)s:%(process)d|%(threadName)s:%(thread)d"
    " - %(message)s",
    datefmt=CUSTOM_TIME_FORMAT,
    project_root=PROJECT_ROOT
)
stream_handler2 = logging.StreamHandler(sys.stdout)
stream_handler2.setFormatter(formatter)

stderr_logger = logging.getLogger('my_project')
stderr_logger.setLevel(logging.DEBUG)
stderr_logger.addHandler(stream_handler2)
stderr_logger.propagate = False