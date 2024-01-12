import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
s, e = 1, 1
hap = 1

while e != n :
    if hap == n: 
        cnt += 1
        e += 1
        hap += e
    elif hap > n:
        hap -= s
        s += 1
    else: 
        e += 1
        hap += e

print(cnt)
