import sys
input = sys.stdin.readline
res = []
t = int(input())
for i in range(t):
    a = int(input())
    room = [1]*a
    for i in range(2,a+1):
        for j in range(1,a+1):
            if i * j > a: 
                continue
            else: 
                if room[i*j-1] == 1:
                    room[i*j-1] = 0
                elif room[i*j-1] == 0:
                    room[i*j-1] = 1
    res.append(room.count(1))
for i in res:print(i)
