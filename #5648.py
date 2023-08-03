arr =[]
while True: 
    try: 
        nums = list(map(str, input().split()))  
        for i in nums: 
            arr.append(i)
    except EOFError: break

arr = arr[1:]
for i,num in enumerate(arr):
    arr[i] = int(num[::-1])
arr.sort()
for i in arr: print(i)
