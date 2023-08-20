import sys

input = sys.stdin.readline

n = input().strip()

if 'M' in n and 'O' in n and 'B' in n and 'I' in n and 'S' in n:
    print('YES')
else: print('NO')
