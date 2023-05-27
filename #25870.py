s = list(map(str, input()))
s_ = set(s)
res = []
for i in s_:
    if s.count(i) %2 == 0:
        res.append(0)
    else: res.append(1)

if len(res) == res.count(0):
    print(0)
elif len(res) == res.count(1):
    print(1)
else: print(2)
