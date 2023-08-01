s = input()
n = int(input())
cnt = 0
for i in range(n):
    a = input()
    if s in a: 
        cnt += 1
    else: 
        if s[0] in a:
            j = a.index(s[0])
            new_a = a[j:]+a[:j]
            
            if s in new_a:cnt += 1

print(cnt)
