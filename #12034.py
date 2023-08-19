import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input().strip())
for i in range(n):
    k = int(input().strip())
    nums = list(map(int, input().split()))
    print(f'Case #{i+1}:',end=' ')  
    res = deepcopy(nums)
    for j in nums: 
        if j%4 == 0: 
            if (j//4) * 3 in res: 
                print((j//4)*3,end=' ')
                res.pop(res.index(j))
                res.pop(res.index((j//4)*3))
           
               
    
    print()
