import sys
input = sys.stdin.readline
n = int(input())
res = []
for i in range(n):
    a = input().strip()
    aa = []
    for i in a:
        if i not in aa:
            aa.append(i)

    res.append(len(aa))
            


for i in res: print(i)
