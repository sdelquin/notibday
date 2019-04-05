import datetime

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import client, file, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'


class GCal:
    def __init__(self, calendar_id):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('calendar', 'v3', http=creds.authorize(Http()))
        self.calendar_id = calendar_id

    def get_events(self, start_datetime=None, end_datetime=None, delta=None):
        if not start_datetime:
            # midday
            start_datetime = datetime.datetime.utcnow().replace(
                hour=12, minute=0, second=0)
        if not end_datetime:
            end_datetime = start_datetime + datetime.timedelta(seconds=1)

        if delta:
            start_datetime = start_datetime + datetime.timedelta(days=delta)
            end_datetime = end_datetime + datetime.timedelta(days=delta)

        start = start_datetime.isoformat() + 'Z'
        end = end_datetime.isoformat() + 'Z'

        events_result = self.service.events().list(
            calendarId=self.calendar_id,
            timeMin=start,
            timeMax=end,
            singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])
        return [(e['start']['date'], e['summary']) for e in events]
