import datetime
import os
import re

from gcal import GCal
from tg import send_message


class NotiBday:
    def __init__(self, calendar_id):
        self.calendar = GCal(calendar_id)

    def notify_today_birthdays(self):
        start_date = datetime.datetime.utcnow().replace(
            hour=0, minute=0, second=0, microsecond=0)
        end_date = start_date + datetime.timedelta(days=1)
        events = self.calendar.get_events(
            start_date=start_date, end_date=end_date)
        if events:
            buf = ['Hoy es el cumpleaños de:']
            for event in sorted(events, key=lambda t: t[1]):
                name = re.split(r'\s*-\s*', event[1])[0]
                buf.append(f'🎂 *{name}*')
            msg = os.linesep.join(buf)
            send_message(msg)
