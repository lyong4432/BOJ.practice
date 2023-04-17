t = int(input())

ans = []
i = 1
for _ in range(t):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] + a[1] > a[2]:
        if a[0] == a[1] == a[2]:
            ans.append(f'Case #{i}: equilateral')
        elif a[0] == a[1] or a[1] == a[2]:
            ans.append(f'Case #{i}: isosceles')
        else: 
            ans.append(f'Case #{i}: scalene')
    else:
        ans.append(f'Case #{i}: invalid!')
    i += 1

for i in ans:
    print(i)
