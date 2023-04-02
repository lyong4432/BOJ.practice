n = int(input())
array = []
for i in range(0,n):
    a = int(input())
    if a%2 == 0:
        array.append('even')
    else:
        array.append('odd')

for i in array:
    print(i)
