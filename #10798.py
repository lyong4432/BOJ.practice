b = ['']*15
for i in range(5):
    a = list(map(str, input()))
    j = 0
    for i in a:
        b[j] += i
        j += 1

for i in b:
    print(i,end='')
