import sys
h, m, s = map(int, sys.stdin.readline().split())
time_s = h * 3600 + m * 60 + s
q = int(input())
for i in range(q):
    t = list(map(int, sys.stdin.readline().split()))
    if t[0] == 1:
        time_s += t[1]
        time_s %= 86400
    elif t[0] == 2:
        time_s -= t[1]
        time_s %= 86400
    elif t[0] == 3:
        hh = time_s//3600
        mm = (time_s%3600)//60
        ss = (time_s%3600)%60
        print(hh,mm,ss)
