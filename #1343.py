string = input()
answer = []
break1 = 0
a = string.split('.')

for i in a: 
    if len(i) %2 != 0: 
        break1 = 1
        break
    else: 
        ans = ''
        length = len(i)
        while length !=0:
            if length >= 4:
                ans +='AAAA'
                length -= 4
            elif length <=2:
                ans += 'BB'
                length -= 2
        answer.append(ans)
if break1 == 1: 
    print(-1)
else:
    for i in answer[:-1]: print(i,end='.')
    print(answer[-1])
