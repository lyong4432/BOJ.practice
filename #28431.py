import sys

input = sys.stdin.readline
res = []
for i in range(5):
    n = input().strip()
    res.append(n)

s_res = set(res)
for i in res: 
    if res.count(i) % 2 != 0:
        print(i)
        break
