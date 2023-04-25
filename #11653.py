n = int(input())
i = 2
ans = []
while i <= n:
    if n%i == 0:
        ans.append(i)
        n //= i
    else: 
        i += 1

for i in ans:
    print(i)
