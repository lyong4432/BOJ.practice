from datetime import datetime

d,m = map(int, input().split())

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(weekdays[datetime(2009,m,d).weekday()])
