import sys
input = sys.stdin.readline
cases = 1
while True:
    n = int(input().strip())
    if n == 0: break
    names = []
    rings = [0]*n
    for i in range(n):
        names.append(input().strip())
    for i in range(2*n-1):
        num, ring = map(str, input().split())
        num = int(num)
        rings[num-1] += 1
    
    no_return = names[rings.index(1)]
    print(cases,no_return) 
    cases += 1  
