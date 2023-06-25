n, m = map(int, input().split())
board = []
go = 0
ans = 0
for i in range(n):
    board.append(int(input()))

for i in range(m):
    a = int(input())
    
    if go < n :
        go += a
        if go < n :
            go += board[go]
        ans += 1
    
print(ans)
