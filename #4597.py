while True:
    a = input()
    if a == "#":
        break
    a = list(a)
    if a[-1] == "e":
        cnt = a.count('1')
        if cnt%2 == 0: 
            a[-1] = '0'
        else: a[-1] = '1' 
    elif a[-1] == "o":
        cnt = a.count('1')
        if cnt%2 == 0: 
            a[-1] = '1'
        else: a[-1] = '0' 

    print(*a,sep='')
