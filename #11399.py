n = int(input())
a = list(map(int, input().split()))
a.sort()
hap = 0
res = []

for i in a: 
    hap += i
    res.append(hap)

print(sum(res))
