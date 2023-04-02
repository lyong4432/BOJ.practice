n = int(input())
array = []
for i in range(0,n):
    a = input()
    a =a[0].upper()+a[1:]
    array.append(a)

for i in array:
    print(i)
