n = input().upper()
string = set(n)
max = 0
for i in string:
    j = n.count(i)
    if j > max:
        max = j
        ans = i
    elif j == max:
        max = j
        ans = '?'    

print(ans)
