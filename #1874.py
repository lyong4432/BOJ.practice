import sys
input = sys.stdin.readline

n = int(input())
A = []
stack = []
for i in range(n):
    A.append(int(input()))

num = 1
result = True
answer = ""

for i in range(n):
    s = A[i]
    if s >= num:
        while s >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else: 
        n = stack.pop()
        
        if n > s: 
            print('NO')
            result = False
            break
        else: answer += "-\n"


if result: print(answer)
