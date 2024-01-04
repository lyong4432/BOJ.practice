import sys
input = sys.stdin.readline

d, k = map(int, input().split())

dp = [[0,0] for _ in range(d)]
dp[0] = [1,0]
dp[1] = [0,1]
for i in range(2,d):
    dp[i] =  [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]



a, b = dp[d-1][0], dp[d-1][1]

for i in range(k):
    if (k - b * i) % a == 0 and (k - b * i) // a <= i:
        print((k - b * i) // a)
        print(i)
        break
