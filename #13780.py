n, k = map(int, input().split())
a = list(map(int, input().split()))
hap = 0
for i in a:
    if i%2 == 0:
        hap += (i//2)
    else: 
        hap += ((i//2)+1)

if hap >= n:
    print('YES')
else:
    print('NO')
