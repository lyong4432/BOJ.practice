ans = []
t = int(input())
for _ in range(t):
    n = int(input())
    n = bin(n)
    n = n.replace('0b','')
    n = str(n)
    reverse_n = n[::-1]
    result = ''
    for i in range(0,len(reverse_n)):
        if reverse_n[i] == '1':
            if i == len(reverse_n) -1:
                result += f'{str(i)}'
            else:
                result += f'{str(i)} '
    ans.append(result)    

        
for i in ans:
    print(i)
