import datetime
import os
import re

from gcal import GCal
from tg import send_message

NEXT_BIRTHDAYS = ((7, 'Falta *1 semana* para el cumpleaños de:'),
                  (15, 'Faltan *15 días* para el cumpleaños de:'),
                  (31, 'Falta *1 mes* para el cumpleaños de:'))


class NotiBday:
    def __init__(self, calendar_id):
        self.calendar = GCal(calendar_id)

    @staticmethod
    def parse_bday_event(event):
        date, summary = event
        if not summary.startswith('Aniversario'):
            name = re.split(r'\s*-\s*', summary)[0]
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
        else:
            name, date = None, None
        return name, date

    def notify_today_birthdays(self):
        start_date = datetime.datetime.utcnow().replace(
            hour=0, minute=0, second=0, microsecond=0)
        end_date = start_date + datetime.timedelta(days=1)
        events = self.calendar.get_events(
            start_date=start_date, end_date=end_date)
        if events:
            buf = ['Hoy es el cumpleaños de:']
            for event in sorted(events, key=lambda t: t[1]):
                name, _ = NotiBday.parse_bday_event(event)
                if name:
                    buf.append(f'🎂 *{name}*')
            msg = os.linesep.join(buf)
            send_message(msg)

    def _get_birthdays_at_delta(self, delta, caption):
        start_date = datetime.datetime.utcnow().replace(
            hour=0, minute=0, second=0, microsecond=0)
        start_date += datetime.timedelta(days=delta)
        end_date = start_date + datetime.timedelta(days=1)
        events = self.calendar.get_events(
            start_date=start_date, end_date=end_date)
        if events:
            buf = [caption]
            for event in sorted(events, key=lambda t: t[1]):
                name, date = NotiBday.parse_bday_event(event)
                if name:
                    date = date.strftime("%-d/%-m")
                    buf.append(f'🎈 *{name}* ({date})')
            msg = os.linesep.join(buf)
        else:
            msg = ''
        return msg

    def notify_next_birthdays(self):
        buf = []
        for next_birthday in NEXT_BIRTHDAYS:
            birthdays = self._get_birthdays_at_delta(*next_birthday)
            if birthdays:
                buf.append(birthdays)
                buf.append(2 * os.linesep)
        if buf:
            send_message(''.join(buf))
