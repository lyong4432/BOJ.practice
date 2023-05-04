n = int(input())
cnt = 0
for i in range(1,n+1):
    j = str(i)
    for u in j:
        if u in ['3','6','9']:
            cnt += 1

print(cnt)
