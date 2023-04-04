arr = []
t = int(input())
for i in range(t):
    a = int(input())
    time = 0
    for j in range(1,a):
        if (j + (j**2)) <= a:
            time = j
    arr.append(time)

for i in arr:
    print(i)
