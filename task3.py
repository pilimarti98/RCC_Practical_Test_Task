#This script contains the resolution of the question 3 from the third task
from datetime import datetime, timedelta
import pytz

#Get the current CET timestamp for exactly one day later
one_day = (datetime.now(pytz.timezone('CET')) + timedelta(days=+1))

#Get the list of all timestamps until the end of the day
end_of_day = one_day.replace(hour=23) + timedelta(hours=1)

hourly_timestamps = []

while one_day <= end_of_day:
    hourly_timestamps.append(one_day)
    one_day += timedelta(hours=1)

# Output list
for ts in hourly_timestamps:
    print(ts.strftime('%Y-%m-%dT%H:00:00Z'))