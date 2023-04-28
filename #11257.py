n = int(input())
ans = []
res =''
for i in range(n):
    a,b,c,d = map(int, input().split())
    hap = b+c+d
    if b>=35*0.3 and c>=25*0.3 and d>=40*0.3 and hap >=55:
        res = 'PASS'
    else:
        res = 'FAIL'
    ans.append(f'{a} {hap} {res}')

for i in ans:
    print(i)

