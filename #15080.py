import datetime as dt
hh, mm, ss = map(int, input().split(':'))
hh1, mm1, ss1 = map(int, input().split(':'))
d = 1 
if hh > hh1 : d += 1
time1 = dt.datetime(2019,1,d,hh,mm,ss)
time2 = dt.datetime(2019,1,d,hh1,mm1,ss1)

sec = time2 - time1

print(sec.seconds)
