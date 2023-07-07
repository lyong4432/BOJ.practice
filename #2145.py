import sys
input = sys.stdin.readline
arr = []
while True:
    n = input().strip()
    if n != '0':            
        arr.append(n)
    else: break

for i in arr: 
    k = i
    while True:
        if len(k) == 1:
            print(k)
            break
        else: 
            new = 0
            for j in k:
                new += int(j)
            k = str(new)
