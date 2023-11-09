def strToOne(i):
    N = list(i)
    hap = 1
    for i in N:
        hap *= int(i)
    i = str(hap)
    print(i,end=' ')  
    if len(i) != 1:
        return strToOne(i)  
    else: print()

            


while True:
    s = input()
    if s =='0': break
    print(s,end=' ')
    if len(s) != 1:
        strToOne(s)
    else: print()
