k = int(input())
hap = 0 
for i in range(1, k+1):
    if k%i == 0:
        hap+= i
print(hap)
