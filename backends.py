import telepot
from django.conf import settings


class TelegramBackend(object):
    def send(self, users, message):
        for user in users:
            message.pk = None
            message.user = user
            message.save()
            bot = telepot.Bot(getattr(settings, 'HLOGGING_TELEGRAM_TOKEN'))
            bot.sendMessage(user.chat_id, message.text[:4095])
