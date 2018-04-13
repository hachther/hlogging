
# HLogging

It is a Django module to receive get notify on telegram when exception occurs.

Follow the steps below to use it:

- Create your bot with bot father on Telegram.
- Install the plugin and set **HLOGGING_TELEGRAM_TOKEN = BOT_TOKEN** in config.
- Now you need to configure users who will receive a Telegram. For that got on the admin panel and configure HLogging user. You will need to have the telegram chat id (to do that send a message to the bot and browse this link [https://api.telegram.org/bot[BOT_TOKEN]/getUpdates](https://api.telegram.org/bot[BOT_TOKEN]/getUpdates)).

Once done, all configured users will receive a Telegram when an exception occurs and the full-log message will be logged.
