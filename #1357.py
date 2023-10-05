import sys

input = sys.stdin.readline
x, y = map(str, input().split())

def rev(i):
    i = i[::-1]
    i = int(i)
    return i 

print(rev(str(rev(x)+rev(y))))
