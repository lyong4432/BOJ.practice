
import sys
arr = []
for i in range(3):
    n = int(sys.stdin.readline())
    sum = 0 
    for _ in range(n):
        a = int(sys.stdin.readline())
        sum += a
    
    if sum == 0:
        arr.append(0)
    elif sum> 0:
        arr.append('+')
    else:
        arr.append('-')

for i in arr:
    print(i)
