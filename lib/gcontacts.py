import datetime

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import client, file, tools

import settings


class GContacts:
    def __init__(self):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', settings.GOOGLE_API_SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('people', 'v1', http=creds.authorize(Http()))

    def retrieve_contacts(self):
        data = (
            self.service.people()
            .connections()
            .list(
                resourceName='people/me',
                pageSize=2000,
                personFields='names,birthdays,emailAddresses',
            )
            .execute()
        )

        self.contacts = {}
        for contact in data['connections']:
            if 'names' in contact.keys():
                full_name = contact['names'][0]['displayName']
                if 'birthdays' in contact.keys():
                    birthday = contact['birthdays'][0]['date']
                    self.contacts[full_name] = datetime.date(**birthday)

    def get_contact_age(self, contact_name):
        birthdate = self.contacts.get(contact_name)
        if birthdate is None:
            return -1
        delta = datetime.date.today() - birthdate
        return round(delta.days / 365)
