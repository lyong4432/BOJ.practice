import math

a,b = map(int, input().split())

result =  [(-1)*a +math.sqrt(a**2-b),(-1)*a -math.sqrt(a**2-b)]
result.sort()
if result[0] == result[1]:
    print('%d'%result[0])
else:
    print('%d %d'%(result[0], result[1]))
