n = int(input())
num = map(int, input().split())
res = 0
for i in num:
    hap = 0
    if i >1:
        for j in range(2,i):
            if i%j == 0:
                hap += 1
        if hap == 0:
            res += 1
    
print(res)
