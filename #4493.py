t = int(input())
result = []
for _ in range(t):
    n = int(input())
    w1 ,w2 = 0,0
    for i in range(n):
        p1 , p2 = map(str, input().split())
        if p1 == 'R':
            if p2 == 'S':
                w1 += 1
            elif p2 == 'P':
                w2 += 1
        elif p1 == 'S':
            if p2 == 'P':
                w1 += 1
            elif p2 == 'R':
                w2 += 1
        elif p1 == 'P':
            if p2 == 'R':
                w1 += 1
            elif p2 == 'S':
                w2 += 1
    if w1 > w2 :
        result.append('Player 1')
    elif w1 == w2:
        result.append('TIE')
    else:
        result.append('Player 2')

for i in result:
    print(i)
