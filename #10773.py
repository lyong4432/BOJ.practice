N = []
for i in range(int(input())):
    a = int(input())
    if a == 0:
        if len(N)!=0:
            N.pop(-1)
    else:
        N.append(a)

print(sum(N))
