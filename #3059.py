n = int(input())
array = []
for i in range(0,n):
    a = input()
    total = 2015
    arr = []
    if a.isalpha():
        for j in a:
            if not(j in arr):
                total -= ord(j)
                arr.append(j)
    array.append(total)

for i in array:
    print(i)
