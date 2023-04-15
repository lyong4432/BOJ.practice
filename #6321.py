alpha = ['A','B','C','D','E','F','G','H','I','J','K','L',"M",'N',"O",'P',"Q",'R','S','T','U','V','W','X','Y','Z']

n = int(input())
result = []
for j in range(n):
    a = input()
    new = ''
    for i in a:
        if i == 'Z':
            new += 'A'
        else:
            new += alpha[alpha.index(i)+1]
    result.append(f'String #{j+1}\n{new}')

for i in result:
    print(i)
    if i != result[-1]:
        print()
