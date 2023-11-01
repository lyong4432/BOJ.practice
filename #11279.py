import sys
import heapq as hq

input = sys.stdin.readline
n = int(input().strip())
N=[]
for i in range(n):
    a= int(input().strip())

    if a == 0: 
        if not N:
            print(0)
        else:
            print(-hq.heappop(N))
    else: hq.heappush(N,-a)


# 최대힙문제 
