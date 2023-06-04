# 시험장의 개수 n 
import sys 
import math

n = int(sys.stdin.readline())
# 각 시험장의 응시자의 수 
a = list(map(int, sys.stdin.readline().split()))

# 한 시험장에서 감시할 수 있는 응시자의 수 B, C명

b, c = map(int, sys.stdin.readline().split())
hap = 0
for i in a:
    hap += 1
    i -= b
    if i >= 1:
        hap += math.ceil(i/c)

print(hap)
