import sys
input = sys.stdin.readline
vowels = ['a','e','i','o','u']
res = []
n = int(input().strip())
for i in range(n):
    n = input().strip()
    n = n.lower()
    c , v = 0 ,0
    for j in n:
        if j in vowels:
            v += 1
        elif j.isalpha(): c += 1
    res.append(f'{c} {v}')

for i in res: print(i)
