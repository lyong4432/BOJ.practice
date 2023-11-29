import sys
input = sys.stdin.readline

def getNext(a):
    arr = list(a)
    idx1 = 0 
    idx2 = 0
    for i in range(1, len(arr)):
          if arr[i-1] < arr[i]:
                if idx1 < i:
                    idx1 = i
    for i in range(1, len(arr)):
          if arr[idx1-1] < arr[i] :
                idx2 = i   
    if idx1 != 0 and idx2 != 0:
        arr[idx1-1], arr[idx2] = arr[idx2], arr[idx1-1]
        arr[idx1:] = list(reversed(arr[idx1:]))
    print(*arr,sep='')
   
    
for i in range(int(input())):
       a = input().strip() 
       getNext(a)
