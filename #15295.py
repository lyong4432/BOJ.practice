t = int(input())
res = []

for i in range(t):
    k,n = map(int, input().split())
    hap = 0
    for i in range(1,n+1):
        hap += i
    hap += n
    res.append(f'{k} {hap}')

for i in res:
    print(i)    
