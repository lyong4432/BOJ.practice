n = int(input())
res = []
for i in range(n):
    s = list(map(str, input().split('-')))
    alpha = (ord(s[0][0])-65)*26**2 + (ord(s[0][1])-65)*26**1 + (ord(s[0][2])-65)
    if abs(alpha-int(s[1]))<=100:
        res.append('nice')
    else: res.append('not nice')

for i in res: print(i)
