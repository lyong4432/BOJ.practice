adrian = 'ABC'
bruno = 'BABC'
goran = 'CCAABB'

n = int(input())
s = input()

adrian = (adrian*n)[:len(s)]
bruno = (bruno*n)[:len(s)]
goran = (goran*n)[:len(s)]
Adrian, Bruno, Goran = 0,0,0
for i in range(len(s)):
    if s[i] == adrian[i]:
        Adrian += 1
    if s[i] == bruno[i]:
        Bruno += 1
    if s[i] == goran[i]:
        Goran += 1

arr = [Adrian, Bruno,Goran]
arr.sort(reverse=True)

max1 = arr[0]
print(max1)
if max1 == Adrian:
    print('Adrian')
if max1 == Bruno:
    print('Bruno')
if max1 == Goran:
    print('Goran')


