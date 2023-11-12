import sys
input = sys.stdin.readline
n = input().strip()
if n[:2] == '0x':
    n = n[2:]
    n = int(n,16)
    print(n)
elif n[:1] == '0':
    n = n[1:]
    n = int(n,8)
    print(n)
else: 
    print(n)
