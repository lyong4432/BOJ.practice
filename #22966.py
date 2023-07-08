n = int(input())
min1 = 5
res = ''
for i in range(n):
    ans, cnt = map(str, input().split())
    cnt = int(cnt)
    if cnt < min1:
        min1 = cnt
        res = ans
        

print(res)
