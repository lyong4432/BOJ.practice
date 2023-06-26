n = int(input())
arr = []

if n == 1: 
    print(1)
else:
    for i in range(1,n+1):
        arr.append(i)
    while True: 
        print(arr[0],end=' ')
        arr.pop(0)
        temp = arr[0]
        arr.pop(0)
        arr.append(temp)
        

        if len(arr) == 1:
            break

    print(arr[0])
