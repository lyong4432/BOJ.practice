import sys
input = sys.stdin.readline

n = int(input().strip())
award = []
for _ in range(n):
    award.append(list(map(int, input().split())))

award.sort(reverse=True, key=lambda x: x[2])

nation = []
for [i,j,k] in award:
    if nation.count(i)<2: 
        print(i,j)
        nation.append(i)
    if len(nation)==3:break
