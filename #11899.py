import sys
input = sys.stdin.readline
s = input().strip()
while True:
    if '()' in s: 
        s = s.replace('()','')
    else: break

print(len(s))
