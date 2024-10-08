from unittest import TestCase

import logging
from utils.logging_tool import CUSTOM_TIME_FORMAT, TimePathFormatter


class TestCustomFormatter(TestCase):

    def test_original_format(self):

        formatter = TimePathFormatter(
            fmt="|%(levelname)-5s|%(asctime)s|%(pathname)s|%(module)s:%(lineno)d|%(name)s - %(message)s"
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)


        logging.basicConfig(
            level=logging.INFO,
            handlers=[stream_handler]
        )
        logger = logging.getLogger("myLogger")
        logger.propagate = True
        logging.info("Test root logger")
        logging.getLogger("myLogger").info("Test logger")

    def test_custom_format(self):

        formatter = TimePathFormatter(
            fmt="|%(levelname)-5s|%(asctime)s|%(relative_path)s|%(module)s:%(lineno)d|%(name)s - %(message)s",
            datefmt=CUSTOM_TIME_FORMAT,
            project_root='/workspace/tests'
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)


        logging.basicConfig(
            level=logging.INFO,
            handlers=[stream_handler]
        )

        logging.info("Test logger")
