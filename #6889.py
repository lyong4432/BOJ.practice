n = int(input())
m = int(input())
nli = []
mli = []
for i in range(n):
    nli.append(input())
for i in range(m):
    mli.append(input())
for i in nli:
    for j in mli:
        print(f'{i} as {j}')
