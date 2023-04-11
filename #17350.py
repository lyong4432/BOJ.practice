n = int(input())
ans = ''
anj = 'anj'

for i in range(n):
    name = input()
    if name in anj:
        ans = '뭐야;'

if ans == '':
    ans = '뭐야?'

print(ans)
    
