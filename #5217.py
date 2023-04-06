t = int(input())

answer = []
for _ in range(t):
    n = int(input())
    a = f'Pairs for {n}: '
    arr = []
    for j in range(1,n):
        for k in range(1,n):
            if (j + k) == n:
                if j < k:
                    arr.append('%d %d'%(j,k))
    for i in arr:
        a += str(i)
        if i != arr[-1]:
            a += ', '
    answer.append(a)

for i in answer:
    print(i)
