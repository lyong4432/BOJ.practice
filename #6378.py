j = 1
ans = []
while j ==1:
    n = input()
    hap = 0
    if n =='0':
        j = 0
    else:    
        for i in range(0,len(n)):
            hap += int(n[i])
        if hap >=10:
            while hap>=10:
                hap = str(hap)
                hap1 = 0
                for i in range(0,len(hap)):
                    hap1 += int(hap[i])
                hap = hap1
                    
        ans.append(hap)

for i in ans:
    print(i)
