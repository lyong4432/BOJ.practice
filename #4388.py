
j =1
ans = []
while j == 1:
    a,b = map(str, input().split())
    if a == '0' and b == '0':
        j = 0
    else:   
        cnt = 0
        a = a[::-1]
        b = b[::-1]
        n = 0 
        if len(a) >= len(b):
            b += '0' * (len(a)-len(b))
            for i in range(0,len(a)):
                if int(a[i]) + int(b[i]) + n>= 10:
                    cnt += 1
                    n = 1
                else:
                    n = 0
        else: 
            a += '0' * (len(b)-len(a))
            for i in range(0,len(a)):
                if int(a[i]) + int(b[i]) + n >= 10:
                    cnt += 1
                    n = 1
                else:
                    n = 0
        ans.append(cnt)

for i in ans:
    print(i)
