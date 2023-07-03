import sys
input = sys.stdin.readline
cm = []
for i in range(9):
    cm.append(int(input()))

diff = sum(cm) - 100
k = 0
for i in cm:
    for j in cm: 
        if i + j == diff and i!=j: 
            cm.pop(cm.index(i))
            cm.pop(cm.index(j))
            k = 1
            break
    if k == 1: 
        break

cm.sort()
for i in cm: 
    print(i)
