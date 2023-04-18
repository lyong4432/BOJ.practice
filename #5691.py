ans = []
j = 1
while j == 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        j = 0
    else: 
        ans.append(2*a - b)

for i in ans:
    print(i)
