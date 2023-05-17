n = int(input())
p = input()
diff = 0
for i in range(0,n//2):
    if p[i] != p[(-1)*(i+1)]:
        diff += 1


print(diff)
