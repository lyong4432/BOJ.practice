from math import ceil
n, m = map(int, input().split())
money = []
set_min = 1000*17
set_left = 1000*5
for i in range(m):
    # 패키지 가격 낱개의 가격
    a, b = map(int, input().split())
    k = [ceil(n/6)*a,n*b]
    money.append(min(k))
    if set_min > (n//6)*a:
        set_min = (n//6)*a
    if set_left > (n%6)*b:
        set_left = (n%6)*b

money.append(set_min+set_left)
print(min(money))
