n = int(input())
money = 0
for i in range(n):
    h, b, k = map(int, input().split())
    if b-h > 0:
        money += (b-h)*k


print(money)
