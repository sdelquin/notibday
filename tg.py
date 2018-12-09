import telegram
import config


def send_message(msg):
    bot = telegram.Bot(token=config.TELEGRAM_BOT_TOKEN)
    bot.send_message(
        chat_id=config.TELEGRAM_USER_ID,
        text=msg,
        parse_mode=telegram.ParseMode.MARKDOWN
    )
