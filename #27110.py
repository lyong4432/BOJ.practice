n =int(input())
a = list(map(int, input().split()))
sum = 0

for i in a:
    if i<=n:
        sum+=i
    else: 
        sum+=n

print(sum)
