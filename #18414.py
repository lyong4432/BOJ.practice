x, l, r = map(int, input().split())
dic = {}
for i in range(l,r+1):
    dic[abs(x-i)] = i

print(dic[min(dic.keys())])
