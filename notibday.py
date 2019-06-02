import datetime
import os
import re

import config
from gcal import GCal
from gcontacts import GContacts
from tg import send_message

NEXT_BIRTHDAYS = ((7, 'Falta *1 semana* para el cumpleaños de:'),
                  (15, 'Faltan *15 días* para el cumpleaños de:'),
                  (31, 'Falta *1 mes* para el cumpleaños de:'))


class NotiBday:
    def __init__(self):
        self.calendar = GCal(config.CONTACTS_CAL_ID)
        self.agenda = GContacts()
        self.agenda.retrieve_contacts()

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
        events = self.calendar.get_events()
        if events:
            buf = ['Hoy es el cumpleaños de:']
            for event in sorted(events, key=lambda t: t[1]):
                name, _ = NotiBday.parse_bday_event(event)
                if name:
                    age = self.agenda.get_contact_age(name)
                    buf.append(f'🎂 *{name}* ({age})')
            msg = os.linesep.join(buf)
            send_message(msg)

    def _get_birthdays_at_delta(self, delta, caption, use_vip=True):
        try:
            with open(config.VIP_FILE) as f:
                vips = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            use_vip = False
        events = self.calendar.get_events(delta=delta)
        if events:
            buf = []
            for event in sorted(events, key=lambda t: t[1]):
                name, date = NotiBday.parse_bday_event(event)
                if name and ((not use_vip) or (use_vip and name in vips)):
                    date = date.strftime("%-d/%-m")
                    age = self.agenda.get_contact_age(name)
                    buf.append(f'🎈 *{name}* ({date}) _{age} años_')
            if buf:
                buf.insert(0, caption)
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
