n = int(input())
res = []
for i in range(n):
    s = input()
    hap = 0
    for i in s:
        if i.isalpha():
            hap += ord(i)-64
    if hap == 100:
        res.append('PERFECT LIFE')
    else: res.append(hap)

for i in res: print(i)
