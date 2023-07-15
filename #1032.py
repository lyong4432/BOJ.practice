n = int(input())
res = []
for i in range(n):
    a = input()
    res.append(a)
    l = len(a)

a = res[0]
word = ''
for i in range(l):
    cnt = 0
    for j in res[1:]:
        if a[i] != j[i]:
            cnt += 1
    if cnt != 0:
        word += '?'
    else: word += a[i]

print(word)
