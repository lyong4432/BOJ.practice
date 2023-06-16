from math import ceil
n = int(input())
files = list(map(int, input().split()))
cluster = int(input())
result = 0
for i in files: 
    if i == 0:
        continue
    else: 
        result += ceil(i/cluster)*cluster

print(result)
