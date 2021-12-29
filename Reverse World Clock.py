#Method 2
from datetime import date
from datetime import datetime
#Show current time
today=date.today()
timethen=datetime.now().replace(microsecond= 0)
print("today's date is ",today)
print('Time is ',timethen)
print("A sample date to input")
print("2021-12-29 11:28:00")
entertime= input("Enter the time of the day (yyyy-mm-dd hh:mm:ss)")
timetaken=datetime.strptime(entertime, '%Y-%m-%d %H:%M:%S')
print("Date: ", timetaken.date())
print("Time: ", timetaken.time())
if str(timetaken) > str(timethen):
    timediff=str(timetaken -timethen)
    ahead=1
    print('Time Difference=', str(timetaken -timethen))
    print("We know the region is in west")
else:
    timediff=str(timethen-timetaken)
    ahead=0
    print('Time Difference=', str(timethen-timetaken))
    print("So we know that the region is in east")
print('Total difference in minutes: ', timediff)
timedifflist=timediff.split(":")
#print(timedifflist)
totalmins=(int(timedifflist[0])*60)+int(timedifflist[1])
print(totalmins)