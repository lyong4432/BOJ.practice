w, l = 0, 0
for i in range(6):
    n = input()
    if n == 'W':
        w += 1
    elif n == 'L':
        l += 1

if w >=5:
    print(1)
elif w>=3:
    print(2)
elif w>=1:
    print(3)
elif l == 6:
    print(-1)
