import subprocess
import re
import datetime
import telegram
import config


def get_contacts():
    today = datetime.datetime.today()
    tomorrow = today + datetime.timedelta(days=1)
    output = subprocess.check_output([
        "gcalcli",
        "agenda",
        today.strftime("%m/%d/%Y"),
        tomorrow.strftime("%m/%d/%Y"),
        "--calendar=Contacts",
        ]
    )

    contacts = list()
    for line in output.decode("utf-8").split("\n"):
        r = re.search(r"(\S+( \S+)*) - Cumpleaños", line)
        if r:
            contacts.append(r.group(1))
    return contacts


def send_message(msg):
    bot = telegram.Bot(token=config.TELEGRAM_BOT_TOKEN)
    bot.send_message(
        chat_id=config.TELEGRAM_USER_ID,
        text=msg,
        parse_mode=telegram.ParseMode.MARKDOWN
    )
