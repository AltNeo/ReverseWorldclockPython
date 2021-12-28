#Method 2
from datetime import date
from datetime import datetime
#Show current time
today=date.today()
timethen=datetime.now()
print("today's date is ",today)
print('Time is ',timethen)
print("A sample date to input")
print("2021-12-28 09:17:27")
entertime= input("Enter the time of the day (yyyy-mm-dd hh:mm:ss)")
timetaken=datetime.strptime(entertime, '%Y-%m-%d %H:%M:%S')
print("Date: ", timetaken.date())
print("Time: ", timetaken.time())
if str(timetaken) > str(timethen):
    print('Time Difference=', str(timetaken -timethen))
else:
    print('Time Difference=', str(timethen-timetaken))
    print("So we know that ")
