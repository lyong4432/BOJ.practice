import sys
input = sys.stdin.readline


k = int(input().strip())
m = 1000000
dp = [0]*(m+1)
for i in range(1,m+1):
    for j in range(i,m+1,i):
        dp[j] += i
    dp[i] += dp[i-1]

for i in range(k):

    n = int(input().strip())
    print(dp[n])
