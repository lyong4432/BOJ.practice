import sys
import time
import datetime as dt
input = sys.stdin.readline


h,m,s=map(int, input().split(":"))
h1,m1,s1=map(int, input().split(":"))

diff = dt.datetime(2020,1,1,h1,m1,s1) - dt.datetime(2020,1,1,h,m,s)
sec = diff.seconds
h2 = sec//3600
m2 = (sec%3600)//60
s2 = (sec%3600)%60

print("%02d:%02d:%02d"%(h2,m2,s2))
