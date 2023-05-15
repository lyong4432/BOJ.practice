n = int(input())
res = []
for i in range(n):
    name, score = map(str, input().split())
    score = int(score)
    g = ''
    if score >= 97:
        g = 'A+'
    elif score >= 90:
        g = 'A'
    elif score >= 87:
        g = 'B+'
    elif score >= 80:
        g = 'B'
    elif score >= 77:
        g = 'C+'
    elif score >= 70:
        g = 'C'
    elif score >= 67:
        g = 'D+'
    elif score >= 60:
        g = 'D'
    else: g = 'F'
    res.append(f'{name} {g}')

for i in res:
    print(i)
