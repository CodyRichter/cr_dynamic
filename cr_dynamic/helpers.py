import datetime

import pytz

def now():
    utc = pytz.timezone('UTC')
    now_utc = utc.localize(datetime.datetime.now())
    return now_utc.astimezone(pytz.timezone('EST'))