import sys
input = sys.stdin.readline

A = [0]*26
B = [0]*26
cnt = 0
a = input().strip()
b = input().strip()
for i in a:
    A[ord(i)-97] += 1
for i in b:
    B[ord(i)-97] += 1
for i in range(26):
    cnt += abs(A[i]-B[i])
print(cnt)
