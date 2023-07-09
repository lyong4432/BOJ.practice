import sys
input=sys.stdin.readline
m, n = map(int, input().split())
mm = list(map(int, input().split()))
nn = list(map(int, input().split()))
total = mm + nn 
total.sort()
for i in total: 
    print(i, end=' ')
