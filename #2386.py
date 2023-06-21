res = []

while True:
    list_x = list(map(str, input()))
    x = list_x[0]
    string = list_x[1:]
  
    cnt = 0
    if x =='#':
        break
    else:
        if x.isupper():
            cnt += string.count(x)
            x1 = x.lower()
            cnt += string.count(x1)
        else: 
            cnt += string.count(x)
            x1 = x.upper()
            cnt += string.count(x1)

        res.append(f'{x} {cnt}')

for i in res: print(i)
