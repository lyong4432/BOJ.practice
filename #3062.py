t = int(input())
for i in range(t):
    a = input()
    aa = a[::-1]
    sum_a = str(int(a)+int(aa))
    # print(sum_a)
    # print(sum_a[:len(sum_a)//2],sum_a[::-1][:len(sum_a)//2])
    if sum_a[:len(sum_a)//2+1] == sum_a[::-1][:len(sum_a)//2+1]:
        print('YES')
    else: print('NO')
