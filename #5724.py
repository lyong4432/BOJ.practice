ans = []
j = 1
while j == 1:
    n = int(input())
    hap = 0
    if n == 0:
        j = 0
    else:
        for i in range(1,n+1):
            hap += (i*i)
        ans.append(hap)

for i in ans:
    print(i)
        
