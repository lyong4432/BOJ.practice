import sys
n = int(sys.stdin.readline().rstrip())

if n == 0:
    n = -1
res = 2432902008176640000
for i in range(20,0,-1):
    res = res//i
    if n >= res:
        n = n - res
    
    
if n == 0:
    print('YES')
else:
    print('NO')
