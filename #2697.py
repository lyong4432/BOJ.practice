import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = input().strip()
    n =  len(a)
    arr = list(a)
    flag = 1
    for i in range(n - 1, 0, -1): 
        if arr[i - 1] < arr[i]: 
            for j in range(n - 1, 0, -1):  
                if arr[i - 1] < arr[j]:  
                    arr[i - 1], arr[j] = arr[j], arr[i - 1]  
                    arr = arr[:i] + sorted(arr[i:])  
                    print(*arr,sep='')  
                    flag = 0
                    break
            if flag == 0: break                   
    if flag == 1: print('BIGGEST') 
