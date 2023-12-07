import sys 
input = sys.stdin.readline
ttt = [[0,0,0] for _ in range(3)]

player = int(input())
flag = 0


def check(ttt, f): 
    if ttt[0][0] == ttt[0][1] == ttt[0][2] ==  f:
        return f
    elif ttt[1][0] == ttt[1][1] == ttt[1][2] ==  f:
        return f
    elif ttt[2][0] == ttt[2][1] == ttt[2][2] ==  f:
        return f
    elif ttt[0][0] == ttt[1][0] == ttt[2][0] ==  f:
        return f
    elif ttt[0][1] == ttt[1][1] == ttt[2][1] ==  f:
        return f
    elif ttt[0][2] == ttt[1][2] == ttt[2][2] ==  f:
        return f
    elif ttt[0][0] == ttt[1][1] == ttt[2][2] ==  f:
        return f
    elif ttt[0][2] == ttt[1][1] == ttt[2][0] ==  f:
        return f
    else: return 0
    

for i in range(9):
    x, y = map(int, input().split())
    if player == 1: 
        if flag == 0:
            ttt[x-1][y-1] = 1
            flag = check(ttt,1)
        player = 2
    elif player == 2: 
        if flag == 0:
            ttt[x-1][y-1] = 2
            flag = check(ttt,2)
        player = 1



print(flag)
