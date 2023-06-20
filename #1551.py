n, k = map(int, input().split())
num = list(map(int, input().split(',')))

# num[1]-num[0],num[2]-num[1],num[3]-num[2],num[4]-num[3]

for j in range(k):
    for i in range(len(num)-1):
        num[i] = num[i+1] - num[i]

    num = num[:-1]

for i in num[:-1]: 
    print(f'{i},',end='')
print(num[-1])
