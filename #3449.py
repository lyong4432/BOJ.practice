res = []
n = int(input())
for i in range(n):
    a = input()
    b = input()
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j]:
            cnt += 1
    res.append(f'Hamming distance is {cnt}.')

for i in res: print(i)
