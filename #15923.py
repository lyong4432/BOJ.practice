n = int(input())
res = []
for i in range(n):
    a,b = map(int, input().split())
    res.append([a,b])

hap = 0 
for i in range(n-1):
    if res[i][0] == res[i+1][0]:
        hap += abs(res[i][1]-res[i+1][1])
    elif res[i][1] == res[i+1][1]:
        hap += abs(res[i][0]-res[i+1][0])

if res[n-1][0] == res[0][0]:
    hap += abs(res[n-1][1]-res[0][1])
elif res[n-1][1] == res[0][1]:
    hap += abs(res[n-1][0]-res[0][0])

print(hap)
