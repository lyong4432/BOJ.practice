n = int(input())
s = input()
res = ''
for i in s[::n]:
    res += i

print(res)
