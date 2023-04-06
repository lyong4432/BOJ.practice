n, t = map(int, input().split())
a = map(int, input().split())
count = 0
sum  = 0
for i in a:
    sum += i
    if sum <= t:
        count += 1
    else: 
        sum -= i
        break

print(count)
