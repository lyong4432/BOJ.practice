n = input()
pre = 0
boolean = 1
for i in range(len(n)-1):
    dis = int(n[i])-int(n[i+1])
    if i>0:
        if pre != dis: 
            boolean = 0
            break
    pre = dis

if boolean == 1: print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
else: print('흥칫뿡!! <(￣ ﹌ ￣)>')
