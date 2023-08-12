import sys
from itertools import combinations
input = sys.stdin.readline
result = {}
n = int(input().strip())
for j in range(n):
    res = []
    cards = list(map(int, input().split()))
    for i in combinations(cards, 3):
        res.append(sum(i)%10)

    result[j+1] = max(res)

result = dict(sorted(result.items(), key=lambda x: x[0], reverse=True))
result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
first_key = next(iter(result))
print(first_key)
