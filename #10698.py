t = int(input())
res = []
for i in range(t):
    n = list(map(str, input().split()))
    result = 0
    if n[1] == '+':
        result = int(n[0]) + int(n[2])
    elif n[1] == '-':
        result = int(n[0]) - int(n[2])
    if result != int(n[4]):
        res.append(f'Case {i+1}: NO')
    else: 
        res.append(f'Case {i+1}: YES')



for i in res:
    print(i)
