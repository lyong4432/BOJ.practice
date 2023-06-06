a, b = map(str, input().split())
hap1, hap2 = 0, 0
for i in a:
    hap1 += int(i)
for j in b:
    hap2 += int(j)

print(hap1*hap2)
