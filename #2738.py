n, m = map(int, input().split())
b = []
for i in range(n):
    a = list(map(int, input().split()))
    b.append(a)
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        b[i][j] += a[j]

for i in b:
    for j in i:
        print(j, end = ' ')
    print()
