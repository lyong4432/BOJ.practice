s = input()

for i in s: 
    if i.isalpha():
        if i.isupper():
            i = ord(i)+13
            if i>90: 
                i -= 26
        else: 
            i = ord(i)+13
            if i>122:
                i -= 26
        print(chr(i),end='')
    else: print(i,end='')
