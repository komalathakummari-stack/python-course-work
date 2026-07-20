'''
from datetime import date,time,datetime,time

t=date.today()

print(t)
print("year:",t.year)
print("month:",t.month)
print("day:",t.day)
print("weekday from 0:", t.weekday())
print("weekday from 1:", t.isoweekday())

'''
'''
from datetime import date,time,datetime,time

t = date(2026,2,4)

print(t)

'''
'''
from datetime import date,time,datetime,time

t=time(20,39,40)

print(t)
'''
'''
from datetime import date,time,datetime,time

n = datetime.now()

print(n)

print("year:", n.year)
print("month:", n.month)
print("day:", n.day)
print("hour:", n.hour)
print("minute:", n.minute)
print("second:", n.second)
print("microsecond:", n.microsecond)

'''

from datetime import date,time,datetime,time

n = datetime.now()

print(n.strftime('%d/%m/%y'))
print(n.strftime('%d/%m/%y %H:%M:%S'))
print(n.strftime('%d/%m/%y %I:%M:%S:%p'))
print(n.strftime('%d %b %y %I:%M:%S:%p'))
print(n.strftime('%d %B %Y %I:%M:%S:%p'))
print(n.strftime('%a, %d %B,%Y %I:%M:%S: %p'))
print(n.strftime('%A, %d %B,%Y %I:%M:%S: %P'))

'''
from datetime import date,time,datetime,timedelta

n = datetime.now()

n15 = n+timedelta(minutes=15)
n2 = n+timedelta(hours=2)
n7 = n+timedelta(days=15)

print(n15,n2,n7,sep='\n')
'''




































