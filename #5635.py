import sys
import datetime as dt
input = sys.stdin.readline
n = int(input().strip())
liveDate = {}
for i in range(n):
    name, dd, mm, yyyy = map(str, input().split())
    now = dt.datetime.now()
    dd = int(dd)
    mm = int(mm)
    yyyy = int(yyyy)
    years = now - dt.datetime(yyyy,mm,dd)
    liveDate[name] = years.days

liveDate = dict(sorted(liveDate.items(), key=lambda x: x[1]))

print(list(liveDate.keys())[0])
print(list(liveDate.keys())[-1])
