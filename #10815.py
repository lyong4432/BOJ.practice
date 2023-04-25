import sys
n = int(sys.stdin.readline())
list_n = set(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
list_m = list(map(int, sys.stdin.readline().split()))
dic = {}
for i in list_m:
    if i in list_n:
        dic[i] = 1
    else: 
        dic[i] = 0
    
print(*dic.values())
