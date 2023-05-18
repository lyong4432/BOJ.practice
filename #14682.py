n = int(input())
k = int(input())
hap = 0
for i in range(0,k+1):
    hap += n * (10**i)

print(hap)
