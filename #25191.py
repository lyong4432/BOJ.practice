import sys

input = sys.stdin.readline
n = int(input().strip()) # 치킨
a, b = map(int, input().split()) #콜라, 맥주

# 콜라 2개에 치킨 하나, 맥주 1개에 치킨 하나 

a //= 2
cnt = 0
cnt = a+b

if n > cnt: print(cnt)
else: print(n)
