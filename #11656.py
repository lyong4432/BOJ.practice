import sys

input = sys.stdin.readline
N = []
s = input().strip()

for i in range(len(s)):
    N.append(s[i:])

N.sort()
print(*N,sep='\n')
