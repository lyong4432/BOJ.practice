n = int(input())
a = list(map(int, input().split()))
y,m = 0, 0

for i in a:
    y += ((i//30 +1)*10)
    m += ((i//60+ 1)*15)

if y>m:
    print('M',m)
elif y<m:
    print('Y',y)
else:
    print('Y M',y)
