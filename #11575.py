import sys

input = sys.stdin.readline

for _ in range(int(input().strip())):
    a,b = map(int, input().split())
    s = input().strip()
    for i in s:
        r = (a*(ord(i)-65)+b)%26
        print(chr(r+65),end='')

    print()
