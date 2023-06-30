import sys
s = sys.stdin.read().replace('\n', '').replace(' ', '') 

c = [0]*26
for i in s: 
    c[ord(i)-97] += 1

max1 = max(c)
res = []

for i in range(26):
    if c[i] == max1:
        res.append(chr(i+97))

res.sort()
for i in res: 
    print(i,end='')
