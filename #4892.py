j = 1
ans = []

while j == 1:
    n = int(input())
    e_o = ''
    if n == 0:
        j = 0
    else:
        n1 = 3 * n
        if n1%2 == 0:
            n2 = n1/2
            e_o = 'even'
        else:
            n2 = (n1 + 1)/2
            e_o = 'odd'
        n3 = 3 * n2
        n4 = n3 // 9 

        if e_o == 'even':
            ans.append(f'even {int(n4)}')
        else: 
            ans.append(f'odd {int(n4)}')
i = 1
for k in ans:
    print(f'{i}. {k}')
    i += 1
