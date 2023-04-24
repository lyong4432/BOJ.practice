t = int(input())
ans = []
for i in range(t):
    a = list(map(int, input().split()))
    aver = sum(a[1:])/a[0]
    cnt = 0
    for i in a[1:]:
        if i >aver:
            cnt += 1
    ans.append(f'{cnt/a[0]*100:.3f}%')


for i in ans:
    print(i)
