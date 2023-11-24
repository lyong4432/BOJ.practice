import sys

input = sys.stdin.readline



n = int(input())
for i in range(n):
    s = input().strip()
    if s[:10] == 'Simon says': 
        print(s[10:])
