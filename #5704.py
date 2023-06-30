res = []

while True: 
    a = input()
    if a == "*": break
    else: 
        j = 1
        for i in range(97,123):
            if chr(i) not in a: 
                j = 0
                break
        if j == 1: 
            res.append('Y')
        else: res.append('N')

for i in res: print(i)
