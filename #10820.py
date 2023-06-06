res = []
while True:
    try: 
        s = list(map(str, input()))
        down, up, digit, space = 0,0,0,0
        for i in s: 
            if i.isupper():
                up += 1
            elif i.islower():
                down += 1
            elif i.isdigit():
                digit += 1
            elif i == ' ':
                space += 1
        res.append(f'{down} {up} {digit} {space}')
    except EOFError:
        break

for i in res: print(i)
