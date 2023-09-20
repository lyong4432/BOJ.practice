import sys

input = sys.stdin.readline
n = int(input().strip())
A = set(map(int, input().split())) # ->탐색시간 줄이기 위해서 set 사용
m = int(input().strip())
B = list(map(int, input().split()))

for i in B:
    if i in A:
        print(1)
    else: print(0)
