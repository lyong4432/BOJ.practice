import sys
n = int(input())
s = list(map(str, sys.stdin.readline().split()))

cnt = 0

for i in s:
    if i in ['he','him','she','her']:
        cnt += 1

print(cnt)
