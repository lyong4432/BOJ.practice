import sys
input = sys.stdin.readline
T  = int(input())
square = 0
for i in range(1, T+1):
    chk = []
    for j in range(2, i//2+1):
        if i % j == 0:
            if j in chk:
                break
            else:
                square += 1
                chk.append(i//j)
    square += 1
print(square)

# 블로그 참고하고 이해 함.. 
