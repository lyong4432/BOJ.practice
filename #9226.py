import sys
input = sys.stdin.readline
mo = ['a','e','i','o','u']
while True:
    s = input().strip()
    if s == '#': break
    new = s
    for i in s: 
        if i not in mo: 
            new = new[1:] + new[0]
        else: break
    print(f'{new}ay')

