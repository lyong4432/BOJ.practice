import sys
input = sys.stdin.readline
n = int(input().strip())

for i in range(n):
    s = input()
    res = [0]*26
    s= s.upper()
    for j in s: 
        if j.isalpha(): 
            res[ord(j)-65] += 1
   
    if res.count(0) != 0: print(f'Case {i+1}: Not a pangram')
    else:
        cnt2,cnt3 = 0,0
        for j in res: 
            if j >= 2: cnt2 +=1
            if j >= 3: cnt3 +=1
        
        print(f'Case {i+1}:',end=' ')
        if cnt3==26: print('Triple pangram!!!')
        elif cnt2==26: print('Double pangram!!')
        else: print('Pangram!')
   
