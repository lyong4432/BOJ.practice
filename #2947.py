arr = list(map(int, input().split()))

while True: 
    for i in range(4):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)
    
    if arr == [1,2,3,4,5]:
        break
