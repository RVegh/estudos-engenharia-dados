from datetime import *
import pytz #Timezone lib

#Take current datetime and use strftime function to defined format
current_time = datetime.today().strftime('%d-%m-%Y %H:%M')
print('Current datetime w/ format:', current_time)

#Also takes current datetime
current_day = datetime.now()
print('Current datetime w/ any format:', current_day)

#Format datetime only with desired date parts
print('Current date: {}/{}/{}'.format(current_day.day, current_day.month, current_day.year))

#Format time using defined delta(sum, subtraction of time(seconds, minutes, hours, etc))
delta = current_day - timedelta(hours=1)
print(f'Current hour: {current_day} \nDelta -1 hour: {delta}')

#Manipulating timezone
'''
For loop to return all timezones:
    for tz in pytz.all_timezones:
        print(tz)
'''
to_timezone = pytz.timezone('Asia/Tokyo')
new_timezone = current_day.astimezone(to_timezone)
print(f'Brazil timezone: {current_day} \nTokyo timezone: {new_timezone}')



