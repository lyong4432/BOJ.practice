import sys
input = sys.stdin.readline
n = int(input().strip())
N = []
nums = list(map(int, input().split()))

for i,j in enumerate(nums):
    N.insert(j,i+1)
N.reverse()
print(*N)
