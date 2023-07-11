import sys
input = sys.stdin.readline
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    max = 0
    ans = ''
    for j in range(n):
        a,b = map(str, input().split())
        b = int(b)
        if max < int(b):
            max = int(b)
            ans = a
    print(ans)
