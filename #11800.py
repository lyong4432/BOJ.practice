import sys 
input = sys.stdin.readline

names = ['Yakk','Doh','Seh','Ghar','Bang','Sheesh']
names_2 = ['Habb Yakk','Dobara','Dousa','Dorgy','Dabash','Dosh']
for i in range(int(input().strip())):
    a,b = map(int, input().split())
    if a>b: b,a=a,b
    if a == b: 
        result = names_2[a-1]
    elif a == 5 and b == 6: result = 'Sheesh Beesh'  
    else: result = f'{names[b-1]} {names[a-1]}'

    print(f'Case {i+1}: {result}')
