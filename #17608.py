import sys

input = sys.stdin.readline
n = int(input())
cnt = 1
pole = []
for i in range(n):
    pole.append(int(input()))

pole.reverse()
max  = pole[0]

for i in range(1,len(pole)):
    if pole[i] > max :
        max = pole[i]
        cnt += 1

print(cnt)
