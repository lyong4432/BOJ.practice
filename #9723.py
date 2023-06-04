import sys 
n = int(sys.stdin.readline())
res = []
for i in range(n):
    a= list(map(int, sys.stdin.readline().split()))
    a.sort()
    if a[0]**2 + a[1]**2 == a[2]**2:
        res.append(f'Case #{i+1}: YES')
    else: res.append(f'Case #{i+1}: NO')
    
for i in res: print(i)
