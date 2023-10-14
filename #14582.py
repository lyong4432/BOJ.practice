import sys

input = sys.stdin.readline
J = list(map(int, input().split()))
S = list(map(int, input().split()))
f = 0
j,s =0,0
for i in range(9):
    j += J[i]
    if j>s:
        f=1
    s += S[i]    

if f: print("Yes")
else: print('No')
