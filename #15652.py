# itertools의 product 사용 -> 시간초과

import sys
from itertools import product
input = sys.stdin.readline
# 중복 순열 
n,m = map(int, input().split())
N = [i for i in range(1,n+1)]

for p in product(N,repeat=m):
    f = 1
    if len(p)>1:
        pre = p[0]
        for j in p[1:]:
            if pre <= j:
                pre = j
            else: 
                f = 0
                break
    if f == 1:                    
        print(*p,sep=' ')


# dfs 사용하는 분들도 많던데 함수가 이미 있으면 그걸 써야지~

import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n,m = map(int, input().split())
N = [i for i in range(1,n+1)]

for p in combinations_with_replacement(N,m):
    print(*p,sep=' ')
