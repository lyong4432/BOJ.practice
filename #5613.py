
sum = 0 
j = 1
cal = ''
while j == 1:
    a = input()
    if a == '=':
        j = 0
    if a.isdigit():
        if cal == '':
            sum = int(a)
        elif cal == '+':
            sum += int(a)
        elif cal == '-':
            sum -= int(a)
        elif cal == '*':
            sum *= int(a)
        elif cal == '/':
            sum //= int(a)    
    else: 
        cal = a

print(sum)

