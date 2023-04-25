n = int(input())
ans = []
for i in range(n):
    t = input()
    if t[len(t)//2-1] == t[len(t)//2]:
        ans.append('Do-it')
    else:
        ans.append('Do-it-Not')    

for i in ans:
    print(i)
