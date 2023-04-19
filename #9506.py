j = 1
ans = []
while j == 1:
    n = int(input())
    if n == -1:
        j = 0
    else: 
        hap = 1
        word = '= 1'
        for i in range(2,n):
            if n%i == 0:
                hap += i
                word += f' + {i}'
        if hap == n:
            ans.append(f'{n} {word}')
        else: 
            ans.append(f'{n} is NOT perfect.')

for i in ans:
    print(i)

        







