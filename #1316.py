n = int(input())
cnt = 0

for _ in range(n):
    a = input()
    pre = a[0]
    stri = []
    c= 1
    stri.append(pre)
    for i in a[1:]:
        if pre == i:
            pass
        else: 
            if i in stri:
                c = 0
            stri.append(i)
        pre = i

    if c == 1:
        cnt += 1
    
print(cnt)
