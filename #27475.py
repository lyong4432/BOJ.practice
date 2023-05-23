t = int(input())
res = []
for i in range(t):
    n, m = map(int, input().split())
    cnt = 0
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    for j in n_list:
        if j in m_list:
            cnt += 1
    res.append(cnt)

for i in res:
    print(i)
