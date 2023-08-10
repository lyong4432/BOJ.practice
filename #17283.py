import sys
input = sys.stdin.readline
l = int(input().strip())
r = int(input().strip())
hap = 0 
i = 1
while True: 
    n = int(l * ( r/ 100))
    if n <= 5: break
    hap += (2**i)*n
    l = n
    i += 1

print(hap)
