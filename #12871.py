from math import lcm
s = input()
t = input()

ls = len(s)
lt = len(t)

c = lcm(ls,lt)

ls = c//ls
lt = c//lt

s = s * ls
t = t * lt

if s == t:
    print(1)
else: print(0)

# 이 문제는 답 주워먹었어요.. 
