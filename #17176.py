import sys
input = sys.stdin.readline
n = int(input().strip())
code = list(map(int,input().split()))
s = input().strip()


# 원래 아스키 코드 
# A-Z : 65-90 a-z : 97-122
# 문제 코드 
# A-Z : 1-26, a-z : 27-52
arr=[]
for i in s: 
    if i.isupper():
        arr.append(ord(i)-64)
    elif i.islower():
        arr.append(ord(i)-70)
    elif i == ' ':
        arr.append(0)
code.sort()
arr.sort()
if code==arr:  print('y')
else: print('n')
