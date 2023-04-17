t = int(input())
result = []
for i in range(t):
    n, c = map(str, input().split())
    result.append(c*int(n))

for i in result:
    print(i)
