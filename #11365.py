j = 1
ans = []
while j == 1:
    n = input()
    if n == 'END':
        j = 0
    else:
        ans.append(n[::-1])

for i in ans:
    print(i)
