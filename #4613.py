while True: 
    a = input()
    if a =="#":
        break
    else: 
        quicksum = 0
        for i,j in enumerate(a):
            if j != ' ':
                quicksum += (i+1) * (ord(j)-64)
        print(quicksum)
