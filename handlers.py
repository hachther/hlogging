# coding=utf-8
import logging

from django.utils.module_loading import import_string
from django.views.debug import ExceptionReporter

LOGGING_BACKEND = {
    'TELEGRAM': 'hlogging.backends.TelegramBackend'
}


class HLoggingHandler(logging.Handler):
    def __init__(self, types=None):
        logging.Handler.__init__(self)
        self.types = types if types else []

    def emit(self, record):
        from hlogging.models import LoggingUser, LoggingMessage
        try:
            request = record.request
        except Exception:
            request = None

        if record.exc_info:
            exc_info = record.exc_info
        else:
            exc_info = (None, record.getMessage(), None)

        reporter = ExceptionReporter(request, is_email=True, *exc_info)
        html = reporter.get_traceback_html()
        text = self.format(record)
        levelname = record.levelname
        for type in self.types:
            users = LoggingUser.objects.filter(type=type).all()
            message = LoggingMessage(level=levelname, text=text, html=html)
            backend = import_string(LOGGING_BACKEND.get(type))()
            backend.send(users, message)
