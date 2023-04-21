n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = []
for i in a:
    for j in a:
        for k in a:
            if i + j + k <= m:
                if i != j and j != k and k != i:
                    ans.append(i+j+k)

print(max(ans))  
