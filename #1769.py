n = input()

cnt = 0

if len(n) == 1:
    n = int(n)
else:
    while True:
        num = 0
        if len(n) == 1: 
            n = int(n)
            break
        else:
            for i in n:
                num += int(i)
            n = str(num)
            cnt += 1
        
        

print(cnt)
if n % 3 == 0:
    print('YES')
else: print('NO')
