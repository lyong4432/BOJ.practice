n = int(input())
mirror = []
for i in range(n):
    mirror.append(input())
k = int(input())

if k ==1:
    for i in mirror:
        print(i)
elif k ==2:
    for i in mirror:
        print(i[::-1])
elif k ==3:
    for i in reversed(mirror):
        print(i)
