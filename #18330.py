n =  int(input())
k = int(input())

dd = k + 60 

if n <= dd:
    print(n*1500)
else:
    print((n-dd)*3000 + dd*1500)
