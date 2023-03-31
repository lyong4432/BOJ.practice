n =int(input())
array = []
d, p = 0, 0
for i in range(0,n):
    a = input()
    if not(d +2 <= p or p +2 <=d):
        if a == 'D':
            d += 1
        elif a == 'P':
            p += 1
  

print('%d:%d'%(d,p))
