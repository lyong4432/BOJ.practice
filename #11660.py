import sys
input = sys.stdin.readline

n, m = map(int, input().split())
N = []
for i in range(n):
    arr = list(map(int, input().split()))
    N.append(arr)

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 1열 0으로 채우기 
hap = 0 
for i in range(n+1):
    dp[i][0] = 0
# 1행 0으로 채우기 
hap = 0
for i in range(n+1):
    dp[0][i] = 0

# 나머지 채우기 
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + N[i-1][j-1]
# for i in dp:
#     print(*i)



for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] -dp[x1-1][y2] - dp[x2][y1-1]+ dp[x1-1][y1-1])
