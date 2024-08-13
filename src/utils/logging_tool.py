import os
import logging
import time


CUSTOM_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S,%(msecs)03d%z"


class TimePathFormatter(logging.Formatter):

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
        super().__init__(
            fmt, datefmt, style, validate, defaults=defaults
        )
        self.project_root = project_root

    def format(self, record):
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
    