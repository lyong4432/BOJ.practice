t = int(input())
x = 0
ans = []
for _ in range(t):
    space = input()
    n = int(input())
    hap = 0
    for i in range(n):
        hap += int(input())
    if hap % n == 0:    
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)
