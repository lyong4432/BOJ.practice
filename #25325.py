import sys
input = sys.stdin.readline
n = int(input().strip())
nums = list(map(str, input().split()))
res = {}
for i in nums:
    res[i] = 0

for _ in range(n):
    a = list(map(str, input().split()))
    for i in a:
        if i in nums:
            res[i] += 1
sorted_dict = dict(sorted(res.items(), key=lambda x: x[0]))
sorted_dict = dict(sorted(sorted_dict.items(), key=lambda x: x[1], reverse=True))


for i,j in sorted_dict.items():
    print(i,j)
