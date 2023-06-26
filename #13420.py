import sys
input = sys.stdin.readline
t = int(input())
res = []
for i in range(t):
    a,buho,b,equal,c = map(str, input().split())
    a = int(a)
    b = int(b)
    c = int(c)

    if buho == '*':
        if a * b == c:
            res.append('correct')
        else: res.append('wrong answer')
    elif buho == '+':
        if a + b == c:
            res.append('correct')
        else: res.append('wrong answer')
    elif buho == '-':
        if a - b == c:
            res.append('correct')
        else: res.append('wrong answer')
    elif buho == '/':
        if a // b == c:
            res.append('correct')
        else: res.append('wrong answer')
    
for i in res: print(i)
