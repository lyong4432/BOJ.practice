import sys
input = sys.stdin.readline
n = int(input().strip())
k = 1
hap = 0
while True: 
    if n-k > 0: 
        n -= k
        k += 1
    else: break
hap = k+1
if k %2 == 0: 
    
    for i in range(1,k+1):
        if n == i: 
            print(i,hap-1,sep='/')
            break
        else: hap -= 1
else: 
    for i in range(1,k+1):
        if n == i: 
            print(hap-1,i,sep='/')
            break
        else: hap -= 1
