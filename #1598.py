from math import ceil

n,m = map(int, input().split())
n1 = [ceil(m/4),m%4]
n2 = [ceil(n/4), n%4]
if n%4 == 0:
    n2[1] = 4
if m%4 == 0:
    n1[1] = 4

print( abs(n2[0]-n1[0]) + abs(n2[1]-n1[1]))
