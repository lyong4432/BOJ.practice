n, m, k = map(int, input().split())
mlist = list(map(int, input().split()))
klist = list(map(int, input().split()))

print(n - len(mlist) - len(klist))
res = []
gift = mlist + klist 
gift.sort()
for i in range(1,n+1):
    if i not in gift:
        res.append(i)

for i in res:
    print(i, end= " ")
