res = []
for i in range(10):
    a = int(input())
    res.append(a)

aver = int(sum(res)/10)

res_set = set(res)
cnt = 0
for i in res_set:
    if res.count(i) > cnt:
        cnt = res.count(i)
        result = i

print(aver)
print(result)
