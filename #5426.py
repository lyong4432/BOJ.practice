import sys
from math import sqrt
input = sys.stdin.readline

for _ in range(int(input())):
    code = input().strip()
    l = len(code)
    n = int(sqrt(l))
    N = []
    idx = 0
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(code[idx])
            idx += 1
        N.append(arr)


    M = [['' for _ in range(n)] for _ in range(n)]

    for i,arr in enumerate(N):
        for j,arr1 in enumerate(arr):
            M[n-j-1][i] = arr1

    result = ''

    for i in M: 
        for j in i: 
            result += j
    print(result)
