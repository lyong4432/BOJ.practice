import sys
input = sys.stdin.readline
n = int(input().strip())

def convert(s,rule):
    result = ''
    for i in s:
        if i.isalpha():
            result += rule[ord(i)-65]
        else: result += i
    return result

for i in range(n):
    s = input().strip()
    rule = input().strip()
    print(convert(s,rule))
