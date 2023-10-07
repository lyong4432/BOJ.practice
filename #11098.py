import sys

input = sys.stdin.readline
n = int(input().strip())
for _ in range(n):
    dic = {}
    for i in range(int(input().strip())):
        p, name = map(str, input().split())
        dic[name] = int(p)
    dic = dict(sorted(dic.items(),key = lambda x:x[1],reverse=True))
    print(next(iter(dic)))
