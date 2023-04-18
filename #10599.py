ans = []
j = 1
while j == 1:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        j = 0
    else: 
        age = [c-a,c-b,d-a,d-b]
        ans.append(f'{min(age)} {max(age)}')

for i in ans:
    print(i)
