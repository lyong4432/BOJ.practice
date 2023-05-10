n = input()
a = 0
b = 0

for i in range(0,len(n),2):
    if n[i] == 'A':
        a += int(n[i+1])
    elif n[i] == 'B':
        b += int(n[i+1])

    if a >= b + 2 and a>=11:
        print('A')
    elif b>= a+ 2 and b>=11:
        print('B')
