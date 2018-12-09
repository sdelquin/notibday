import datetime
import os
import re

import config
from gcal import GCal
from tg import send_message


def today_birthdays():
    calendar = GCal(config.CONTACTS_CAL_ID)
    start_date = datetime.datetime.utcnow().replace(
        hour=0, minute=0, second=0, microsecond=0)
    end_date = start_date + datetime.timedelta(days=1)
    events = calendar.get_events(start_date=start_date, end_date=end_date)
    if events:
        buf = ['Hoy es el cumpleaños de:']
        for event in sorted(events, key=lambda t: t[1]):
            name = re.split(r'\s*-\s*', event[1])[0]
            buf.append(f'🎂 *{name}*')
        msg = os.linesep.join(buf)
        send_message(msg)


if __name__ == "__main__":
    today_birthdays()
