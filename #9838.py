n = int(input())
res = [0]*n
for i in range(n):
    a = int(input())
    res[a-1] = i+1

for i in res:
    print(i)
