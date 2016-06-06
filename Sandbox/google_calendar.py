from __future__ import print_function
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.discovery import build


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

class GoogleCalendar:
    def __init__(self):
        SCOPES = "https://www.googleapis.com/auth/calendar"
        store = file.Storage('storage.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
            creds = tools.run_flow(flow, store, flags) \
                if flags else tools.run(flow, store)

        CAL = build('calendar', 'v3', http=creds.authorize(Http()))

        GMT_OFF = '+06:00'

        EVENT = {
            'summary': 'Book Renew',
            'start': {'dateTime': '2016-06-28T19:00:00%s' % GMT_OFF},
            'end': {'dateTime': '2016-06-28T22:00:00%s' % GMT_OFF},
        }

        e = CAL.events().insert(calendarId='primary', sendNotifications=True, body=EVENT).execute()

