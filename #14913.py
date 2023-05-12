a, d, k = map(int, input().split())


n = (k - a)/d + 1

if n == 0:
    print('X')
elif float(n) == ((k - a)//d + 1):
    print(int(n))
  
else: print('X')
