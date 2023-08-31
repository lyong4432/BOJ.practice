import sys
input = sys.stdin.readline
n ,m = map(int, input().split())
cnt = n
while True:
    cnt += n//m
    n = n//m
    if n // m == 0:
        break
    
    

print(cnt)
