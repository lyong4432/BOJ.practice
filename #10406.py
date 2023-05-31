w, n, p = map(int, input().split())
hp = list(map(int, input().split()))
cnt = 0
for i in hp:
    if w <= i <= n:
        cnt += 1

print(cnt)
