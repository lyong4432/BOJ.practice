n, m, k = map(int, input().split())
team = 0

while n>1 and m>0 and (m+n-k)>2:
        n -= 2
        m -= 1
        team +=1

print(team)
