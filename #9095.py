import sys
input = sys.stdin.readline


k = int(input().strip())


for i in range(k):
    a = int(input().strip())
    dp = [0] * a
    
    for i in range(a):
        if i == 0 : dp[0] = 1
        elif i == 1: dp[1] = 2
        elif i == 2: dp[2] = 4
        else:dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[a-1])
