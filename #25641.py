n = int(input())
p = list(map(str, input()))

while p.count('s') != p.count('t'):
    p.pop(0)

for i in p:
    print(i, end='')
