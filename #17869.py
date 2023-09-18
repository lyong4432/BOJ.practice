import sys
input = sys.stdin.readline
n = int(input().strip())

cnt = 0
while True:
    if n % 2 == 0:
        n //= 2   
    else: 
        n += 1
    cnt += 1
    if n == 1: break
print(cnt)
