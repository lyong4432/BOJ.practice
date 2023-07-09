import sys
input = sys.stdin.readline
t = int(input().strip())

def living_people(k,n):
    arr = []
    arr1 = []
    for j in range(1,n+1): # 1~n호 
        arr1.append(j) # 0층
    arr.append(arr1)
    if k > 0:
        for i in range(1,k+1): # 1~k-1층 
            arr1 = [1]
            for j in range(1,n):
                arr1.append(arr1[j-1]+arr[i-1][j])
            arr.append(arr1)
    return arr[k][n-1]
        



for i in range(t):
    k = int(input().strip())
    n = int(input().strip())
    print(living_people(k,n))
