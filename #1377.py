import sys 
input = sys.stdin.readline  

n = int(input())
A = []

for i in range(n):
    A.append((int(input()), i))

SA = sorted(A)

m = 0
for i in range(n):
    if m < SA[i][1] - i: m = SA[i][1] - i


print(m + 1)   
