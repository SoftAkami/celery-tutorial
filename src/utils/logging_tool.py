import logging
import time
import os


CUSTOM_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S,%(msecs)03d%z"


class CustomFormatter(logging.Formatter):

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
        # Get the module's path
        module_path = os.path.abspath(record.pathname)
        # Convert it to a path relative to the project root
        relative_path = os.path.relpath(module_path, self.project_root)
        # Include the relative path in the log message
        record.relative_path = relative_path.replace("/", ".")
        return super().format(record)

    def formatTime(self, record, datefmt=None):
        """
        Overwrite `formatTime` to insert `msecs` before timezone offset.
        """
        if datefmt == CUSTOM_TIME_FORMAT:

            ct = self.converter(record.created)
            print(record.msecs)
            s = time.strftime(self.custom_time_format, ct) % {'msecs': int(record.msecs)}
            return s

        return super().formatTime(record, datefmt)
    