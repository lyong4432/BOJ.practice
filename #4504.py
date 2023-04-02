n = int(input())
array = []
j =1
while j == 1:
    a = int(input())
    if a == 0:
        j = 0
    elif a%n == 0:
        array.append('%d is a multiple of %d.'%(a,n))
    else:
        array.append('%d is NOT a multiple of %d.'%(a,n))

for i in array:
    print(i)
