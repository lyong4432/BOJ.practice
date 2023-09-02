N, K = map(int, input().split())
d = []
for j in range(N):
    d.append(int(input()))

ans = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if d[j] >= d[i] and d[j] - d[i] <= K:
            cnt += 1
    ans = max(ans, cnt)

print(ans)

# 도저히 이해가 안 되서 구글링해서 C++로 작성한 코드를 뤼튼에게 파이썬으로 고쳐달라고 함 
