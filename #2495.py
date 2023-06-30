import sys
input = sys.stdin.readline
res = []
for i in range(3):
    s = input().strip()
    max1 = 1
    cnt = 1
    for j in range(1,len(s)):
        if s[j-1] == s[j]:
            cnt += 1
            if cnt > max1:
                max1 = cnt
        else: cnt = 1
    res.append(max1)

for i in res: print(i)
