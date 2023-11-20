import sys 
input = sys.stdin.readline
a,b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

C = list(A - B)
C.sort()
print(len(C))
if len(C) != 0: print(*C)
