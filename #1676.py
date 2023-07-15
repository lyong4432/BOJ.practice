n = int(input())
hap = 1
for i in range(1,n+1):
    hap *= i
cnt = 0
for i in str(hap)[::-1]:
    if i == '0':
        cnt += 1
    else: break

print(cnt)
