k = 1
res = []

while k == 1:
    t = int(input())
    if t == 0:
        k = 2
    else: 
        list_t = list(map(int, input().split()))
        m, j = 0, 0
        for i in list_t:
            if i == 0:
                m += 1
            elif i == 1:
                j += 1
        res.append(f'Mary won {m} times and John won {j} times')

for i in res:
    print(i)
