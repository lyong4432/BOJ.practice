n = int(input())
cnt = []
for i in range(n):
    mm,dd = map(int, input().split('/'))
    a = [mm,dd]
    if a not in cnt:
        cnt.append(a)


print(len(cnt))
