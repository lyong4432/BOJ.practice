n = int(input())
vinu = list(map(int, input().split()))
oppo = list(map(int, input().split()))
v = 0
for i in range(n):
    if vinu[i] > oppo[i]:
        v += 3
    elif vinu[i] == oppo[i]:
        v += 1

print(v)
