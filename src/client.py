import ICalParser

ICAL_LINKS = [
    'https://auburn.instructure.com/feeds/calendars/course_v9skiGjDlv4h2jMnIeK7ebT3KZjBVWo4y9Kusp6o.ics'
]


calendars = ICalParser.getCalendarObject(ICAL_LINKS)
print(calendars)