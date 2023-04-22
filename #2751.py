import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    k = int(sys.stdin.readline())
    a.append(k)

a.sort()

for i in a:
    print(i)
