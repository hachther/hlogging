from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


LOGGING_TYPE = (
    ('TELEGRAM', _('Telegram')),
)


class LoggingUser(models.Model):
    user = models.ForeignKey(getattr(settings, 'AUTH_USER_MODEL'))
    chat_id = models.IntegerField(_('chat id'), null=True, blank=True)
    type = models.CharField(_('type'), max_length=20, choices=LOGGING_TYPE)


class LoggingMessage(models.Model):
    user = models.ForeignKey(LoggingUser)
    date = models.DateTimeField(_('date'), default=timezone.now)
    level = models.CharField(_('level name'), max_length=10)
    module = models.CharField(_('module'), max_length=50, null=True, blank=True)
    process = models.IntegerField(_('module'), null=True, blank=True)
    thread = models.IntegerField(_('thread'), null=True, blank=True)
    text = models.TextField(_('text'))
    html = models.TextField(_('html'), null=True, blank=True)

