import sys

input = sys.stdin.readline

B = []
for _ in range(5):
    B.append(list(map(int, input().strip().split())))

S = []
for _ in range(5):
    S.append(list(map(int, input().strip().split())))

bingo = [[0] * 5 for _ in range(5)]


def check_row():
    res = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[i][j] == 1:
                cnt += 1
        if cnt == 5:
            res += 1
    return res


def check_col():
    res = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[j][i] == 1:
                cnt += 1
        if cnt == 5:
            res += 1
    return res


def check_dia():
    res = 0
    # 오->왼
    cnt = 0
    for i in range(5):
        if bingo[i][5 - i - 1] == 1:
            cnt += 1
    if cnt == 5:
        res += 1
    # 왼->오
    cnt = 0
    for i in range(5):
        if bingo[i][i] == 1:
            cnt += 1
    if cnt == 5:
        res += 1
    return res


cnt = 0
for i in range(5):
    for j in range(5):
        s = S[i][j]
        for y in range(5):
            for x in range(5):
                if B[y][x] == s:
                    cnt = 0
                    bingo[y][x] = 1
                    cnt += check_row()  
                    cnt += check_col() 
                    cnt += check_dia()  
                    if cnt >= 3:
                        print(i * 5 + j + 1)  
                        exit()  

# 내 코드로 많이 틀려서 블로그보고 학습... 
