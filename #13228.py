t = int(input())
res = []

for i in range(t):
    x1,y1,floor1,x2,y2,floor2 = map(int, input().split())
    res.append(f'{floor1 + abs(x2-x1)+ abs(y2-y1) + floor2}')

for i in res:
    print(i)    
