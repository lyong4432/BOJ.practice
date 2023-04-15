t = int(input())
result = []
for i in range(t):
    n, k = map(int, input().split())
    candy = list(map(int, input().split()))
    hap = 0
    for j in candy:
        hap += (j//k)
    result.append(hap)

for i in result:
    print(i)
