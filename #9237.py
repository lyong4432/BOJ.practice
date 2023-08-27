import sys
input = sys.stdin.readline

n = int(input().strip())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

day = 1
day1 = trees[0]
day += day1
days = [] 
dis = 0
day1 -= 1 
if n > 1:
    for j in trees[1:]:
        if j-day1 > dis: 
            dis = j-day1
        day1 -= 1  


print(day+dis+1)
