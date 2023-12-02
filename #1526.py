import sys

input = sys.stdin.readline

n = int(input())
while True:
    f = 1
    for i in str(n):
        if i != '4' and i != '7':
            f = 0
            n -= 1
    if f == 1: 
        print(n)
        break
