t = int(input())
x = 0
ans = []
for _ in range(t):
    a = list(map(int, input().split()))
    b = [a[0]+a[4], a[1] + a[5], a[2] + a[6], a[3] + a[7]]
    if b[0] < 1:
        b[0] = 1
    if b[1] < 1:
        b[1] = 1
    if b[2]<0:
        b[2] = 0
    force = 1 * b[0] + 5 * b[1] + 2 * b[2] + 2 * b[3]
    ans.append(force)

for i in ans:
    print(i)
