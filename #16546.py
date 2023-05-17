import sys
n = int(sys.stdin.readline())
goal = list(map(int, sys.stdin.readline().split()))

sum_n = n*(n+1)//2
goal_sum = sum(goal)
print(sum_n-goal_sum)
