import sys
input = sys.stdin.readline
import itertools
cnt= 0 
while True: 
    
    N = list(map(int, input().split()))
    if N[0] == 0: break 
    if cnt != 0: print()
    arr = N[1:]
    nPr = itertools.combinations(arr, 6)
    for i in list(nPr):
        print(*i)
    cnt += 1
