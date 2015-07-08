#!/usr/bin/env python2
from datetime import datetime, timedelta
from dateutil import parser
import re
from sys import exit
import caldav

# time offset
time_offset = 2
# user
cal_user = 'valentin'
# password
cal_passwd = 'v@l@tuc1'
# define you caldav URL here
caldav_url = \
            "https://{0}:{1}@cloud.rusu.info/remote.php/caldav/calendars/valentin/personal"\
            .format(cal_user, cal_passwd)

# connect to you caldav instance
def connect(url):
    client = caldav.DAVClient(url,ssl_verify_cert=False)
    principal = client.principal()
    return principal.calendars()[0]

# get you next appointment for today

def parse_eventdata(event):
    parsed_event = {}
    for item in event.data.split("\n"):
        if re.match("^DTSTART\;", item):
            dto = parser.parse(item.split(";")[1].split(":")[1])\
                         + timedelta(hours=time_offset)
        if re.match("^SUMMARY\:", item):
            title = item.split(":")[1].rstrip('\r')
    print dto.strftime("%H:%M") + ' ' + title

try:
    calendar = connect(caldav_url)
    latest_event = calendar.date_search(datetime.utcnow(), datetime.now().date() + timedelta(days=1))[-1]
    parse_eventdata(latest_event)
except IndexError:
    print "Nothing to do"
    exit(0)


