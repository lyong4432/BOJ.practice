vowels = ["a","e","i","o","u"]
main = []
while True:
    s = input()
    if s == 'end': break
    else:
        v = 0
        c_v,c = 0,0
        res = []
        no = 0
        pre =''
        for i in s:
            if pre != i:
                if i in vowels:
                    v += 1
                    c_v += 1
                    c = 0
                else: 
                    c_v = 0
                    c += 1

                if c_v >= 3 or c >= 3:
                    no = 1
                    break
            else: 
                if not((pre == 'e' and i =='e') or (pre == 'o' and i == 'o')):
                    no = 1
                    break

            pre = i

            

        if v == 0 or no == 1: main.append(f'<{s}> is not acceptable.')
        else: main.append(f'<{s}> is acceptable.')
        
for i in main:print(i)
