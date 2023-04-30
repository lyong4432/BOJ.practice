import datetime
n, m = map(int, input().split())
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

b = days[datetime.date(2007, n, m).weekday()]
print(b)
