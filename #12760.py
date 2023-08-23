import sys

input = sys.stdin.readline
n, m = map(int, input().split())
card = []
for i in range(n):
    num = list(map(int, input().split()))
    num.sort(reverse=True)
    card.append(num)
player = [0]*n
for i in range(m):
    game =[]
    for j in range(n):
        
        game.append(card[j][i])
    max1 = max(game)
    for j in range(n):
        if max1 == card[j][i]: player[j] += 1


max2 = max(player)
for i,j in enumerate(player): 
    if max2 == j: print(i+1,end=' ')
