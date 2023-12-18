import sys
input = sys.stdin.readline

n = int(input())
m, k = map(int, input().split())
N = list(map(int, input().split()))
N.sort(reverse=True)
total = m * k
cnt = 0 
for i in N: 
    total -= i
    cnt += 1
    if total <= 0: 
        break 

if total <= 0: 
    print(cnt)
else: print("STRESS")
