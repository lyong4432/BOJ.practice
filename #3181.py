n = list(map(str,input().split()))
short = ''
v = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
for i,j in enumerate(n):
    if (j not in v) or i == 0:
        short += j[0].upper()


print(short)
