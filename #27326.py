n = int(input())
m = list(map(int, input().split()))
set_m = set(m)

for i in set_m:
    if m.count(i) == 1:
        print(i)
        break
