import sys
input = sys.stdin.readline

n = int(input().strip())
bong = list(map(int, input().split()))

ans = 0
maxBong = 0
cnt = 0

for b in bong: 
    if b > maxBong:
        maxBong = b
        cnt = 0
    else: cnt += 1
    ans = max(ans,cnt)

print(ans)
