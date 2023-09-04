import sys
input = sys.stdin.readline
n = int(input().strip())
res = []
for i in range(n):
    a = input().strip()
    while True:
        if '()' in a: 
            a = a.replace("()","")
        else: break

    if len(a) == 0: print("YES")
    else: print('NO')

# 왜 이 아이디어를 못 떠올렸을까.. 쉬운 문제였다.. 
