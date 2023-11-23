import sys
from itertools import permutations
input = sys.stdin.readline


while True:
    try: 
        k, n = map(str, input().split())
        n = int(n)
        arr = list(k)
        nPr = permutations(arr, len(arr))
        cnt = 0
        print(f'{k} {n} = ',end='')
        for i in nPr:
            cnt += 1
            if cnt == n:
        
                print(*i,sep='')
                break

        if cnt > n or cnt < n: print("No permutation")
    except :
        break
