arr = []
j = 1
while j == 1:
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        j = 0
    else:
        arr.append('%d %d / %d'%(a//b,a%b,b))

for i in arr:
    print(i)
