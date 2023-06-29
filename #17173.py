n,m = map(int, input().split())
nums = list(map(int, input().split()))
hap = []
for i in range(1,n+1):
    for j in nums:
        if i%j == 0:
            if i not in hap: 
                hap.append(i)

print(sum(hap))
