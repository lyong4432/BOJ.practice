n = int(input())
p = int(input())
res = []

if n >= 20:
    res = [p * 0.75, p - 2000]
elif n>=15:
    res = [p-2000, p * 0.9]
elif n>=10:
    res = [p * 0.9, p - 500]
elif n>=5:
    res = [p-500]
else:
    res = [p]

res.sort()

if res[0]<0:
    print(0)
else:
    print('%d'%res[0])
