t = int(input())
res = []
for _ in range(t):
    h = int(input())
    s = input()
    for i in s:
        if i == 'c':
            h += 1
        elif i == 'b':
            h -= 1
    res.append(f'Data Set {_+1}:\n{h}')

for i in res:
    print(i)
    if i != res[-1]:
        print()
