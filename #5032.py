e, f, c = map(int, input().split())
drink, bin, new = 0,0,0

while e+f>=c:
    drink = (e+f)//c 
    new += drink
    e = (e+f)%c
    f = drink


print(new)
