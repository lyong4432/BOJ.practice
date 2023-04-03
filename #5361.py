n = int(input())
array = []

for i in range(0,n):
    a,b,c,d,e = map(int, input().split())
    sum = a*350.34 + 230.90 * b + 190.55 * c + 125.30 * d + 180.90 * e
    array.append('$%.2f'%sum)
    

for i in array:
    print(i)
