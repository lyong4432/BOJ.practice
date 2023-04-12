s = list(map(int, input().split()))
n = list(map(int, input().split()))
u = list(map(int, input().split()))

price = [0,0,0]
if s[0] * 10 >=5000:
    price[0] = (s[1] * 10) / (s[0] * 10 - 500)
else: 
    price[0] = (s[1] * 10) / (s[0] * 10 )
if n[0] * 10 >=5000:
    price[1] = (n[1] * 10) / (n[0] * 10 - 500)
else: 
    price[1] = (n[1] * 10) / (n[0] * 10 )
if u[0] * 10 >=5000:
    price[2] = (u[1] * 10) / (u[0] * 10 - 500)
else: 
    price[2] = (u[1] * 10) / (u[0] * 10 )


m = price.index(max(price))
if m == 0:
    print('S')
elif m == 1:
    print('N')
elif m == 2:
    print('U')
