n, m = map(int, input().split())
num = []
for i in range(1,n+1):
    num.append(i)
for i in range(m):
    a, b = map(int,input().split())
    num[a-1:b] = reversed(num[a-1:b])

for i in num:
    print(i, end = ' ')
   

