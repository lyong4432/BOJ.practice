import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

hap = 0
for i in x: 
    for j in x:
        hap += abs(i-j)
    
print(hap)


# pypy3로 맞았습니다. python은 시간 초과 
