from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/calendar']


def create_event(card_name, card_content, card_date):
    """Creates an event with inputs based on the card data
    """
    creds = None
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    

    event = {
        'summary': card_name,
        'description': card_content,
        'start': {
            'date': card_date,
        },
        'end': {
            'date': card_date,
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print( 'Event created: %s' % (event.get('htmlLink')) )