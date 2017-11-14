from django.test import TestCase
import logging


class HLoggingLogTest(TestCase):

    def test_logging(self):
        logger = logging.getLogger('django_test')
        logger.debug('test_log')
        print('fisher')
