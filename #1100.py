cnt = 0 

for i in range(0,8):
    a = list(map(str, input()))
    if i % 2 == 0:
        for j in a[::2]:
            if j == 'F':
                cnt += 1
    else: 
        for j in a[1::2]:
            if j == 'F':
                cnt +=1

print(cnt)
