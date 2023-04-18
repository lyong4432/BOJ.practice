n = int(input())
ans = []
for i in range(n):
    a,b = map(str, input().split())
    string = ''
    for i in b:
        string += i*int(a)

    ans.append(string)

for i in ans:
    print(i)
    
