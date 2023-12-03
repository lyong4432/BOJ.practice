import sys

input = sys.stdin.readline

while True:
    s = list(map(str, input().split()))


    if s[0] == '*': break
    first = s[0][0].lower()
    f = 1
    for i in s: 
        if first != i[0].lower():
            f = 0
            break
    if f == 0 : print('N')
    else: print('Y')
