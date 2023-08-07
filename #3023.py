r, c = map(int, input().split())
pattern = []
for i in range(r):
    s = input()
    pattern.append(s)
a, b = map(int, input().split())
res =[]

for i in range(r):
    k = pattern[i]+pattern[i][::-1]
    if i == a-1:
        if k[b-1] == '#': 
            k = k[:b-1] + '.' + k[b:]
        elif k[b-1] == '.':
            k = k[:b-1] + '#' + k[b:]
    res.append(k)

for i in range(r):
    k = pattern[r-i-1]+pattern[r-i-1][::-1]
    if i+r == a-1:
        if k[b-1] == '#': 
            k = k[:b-1] + '.' + k[b:]
        elif k[b-1] == '.':
            k = k[:b-1] + '#' + k[b:]
    res.append(k)


for i in res: print(i)
