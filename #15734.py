import sys

input = sys.stdin.readline

l,r,a = map(int, input().split())
cnt = 0
if l == r:
    cnt = l+r
    if a%2==0:
        cnt += a
    else: cnt += a-1
elif l > r:
    if r + a >= l:  # 5 + 2 >= 3
        cnt = 2*l
        a = a+r-l
        if a%2 ==0: cnt += a
        else: cnt += a-1
    else: cnt = (r+a)*2
   
else: 
    if l + a >= r: 
        cnt = 2*r
        a = a+l-r
        if a%2 ==0: cnt += a
        else: cnt += a-1
    else: cnt = (l+a)*2

print(cnt)
