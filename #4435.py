t = int(input())
res = []
for i in range(t):
    g = list(map(int, input().split()))
    s = list(map(int, input().split()))
    gg = g[0] + g[1]*2 + g[2]*3 + g[3]*3 + g[4]*4 + g[5]*10
    ss = s[0] + s[1]*2 + s[2]*2 + s[3]*2 + s[4]*3 + s[5]*5 + s[6]*10

    if gg == ss:
        res.append(f'Battle {i+1}: No victor on this battle field')
    elif gg > ss: 
        res.append(f'Battle {i+1}: Good triumphs over Evil')
    else: res.append(f'Battle {i+1}: Evil eradicates all trace of Good')


for i in res:
    print(i)
