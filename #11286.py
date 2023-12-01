from heapq import heappush, heappop
import sys
heap = []
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    if n == 0:
        if len(heap) == 0: print(0)
        else: print(heappop(heap)[1])
        
    else: 
        heappush(heap,(abs(n),n))
