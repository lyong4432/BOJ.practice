# 76점 받음
n = int(input())
cnt = 0
for i in range(1,n+1):
    ii = str(i)
    hap = 0
    for j in ii:
        hap += int(j)
    if i%hap == 0:
        cnt += 1

print(cnt)
