n = input()
ans = ''

if n[0] == 'I':
    ans += 'E'
elif n [0] == 'E':
    ans += 'I'

if n[1] == 'N':
    ans += 'S'
elif n [1] == 'S':
    ans += 'N'

if n[2] == 'F':
    ans += 'T'
elif n [2] == 'T':
    ans += 'F'

if n[3] == 'J':
    ans += 'P'
elif n [3] == 'P':
    ans += 'J'

print(ans)
