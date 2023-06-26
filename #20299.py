import sys
input = sys.stdin.readline
n, k ,l = map(int, input().split())
res = []
cnt = 0
for i in range(n):
    one, two, three = map(int, input().split())
    if one + two + three >= k: 
        if one >=l and two >= l and three >=l:
            cnt += 1
            res.append(one)
            res.append(two)
            res.append(three)
print(cnt)
for i in res: print(i,end=' ')
