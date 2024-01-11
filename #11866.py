import sys
input = sys.stdin.readline

n, k = map(int, input().split())

N = [i for i in range(1,n+1)]
idx = 0
cnt = 0
print('<',end = '')
while len(N)!= 0:
    if cnt == k - 1 : 
        a = N[idx]
        if len(N) == 1:
            print(a,end='>')
        else: print(a,end=', ')
        N.pop(N.index(a))
        cnt = 0
        
    else: 
        idx += 1
        cnt += 1

    if idx == len(N): 
        idx = 0
