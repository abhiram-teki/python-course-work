from datetime import *
'''
today=date.today()
print(today)
print(today.year)
print(today.month)
print(today.weekday())
print(today.isoweekday())
'''
'''
print(date(2026,10,29))
print(time(14,46,10))
print(time(14,46,10).hour)
print(time(14,46,10).minute)
print(time(14,46,10).second)
'''

now=datetime.now()
'''
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
'''
'''
print(now.strftime('%d/%m/%Y'))
print(now.strftime('%d/%m/%Y %H:%M:%S'))
print(now.strftime('%d/%m/%Y %I:%M:%S'))
print(now.strftime('%d/%m/%Y %I:%M:%S %p'))
print(now.strftime('%a %d %b %Y %I:%M:%S %p'))
print(now.strftime('%A %d %B %Y %I:%M:%S %p'))
'''

t_n=now - timedelta(days=30)
print(t_n)




