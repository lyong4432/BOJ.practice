import sys

input = sys.stdin.readline


N = {}
for j in range(int(input())):
    k = int(input())
    if k in N.keys():
        N[k] += 1
    else: N[k] = 1
N = dict(sorted(N.items(),key=lambda x: x[0]))
N = dict(sorted(N.items(),key=lambda x: x[1] , reverse=True))
first_key = next(iter(N))
print(first_key)
    
