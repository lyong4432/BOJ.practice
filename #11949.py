import sys
input = sys.stdin.readline

n, m = map(int, input().split())

t = []

for i in range(n):
    a = int(input())
    t.append(a)

for i in range(1, m+1):
    for idx in range(1,len(t)):
        if t[idx-1] %i > t[idx]%i:
            t[idx-1] ,t[idx] = t[idx], t[idx-1]

for i in t: 
    print(i)
