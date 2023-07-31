import sys
input = sys.stdin.readline
a, b = map(str, input().split())
n = len(a)
m = len(b)
nn = 0
mm = 0
for i in a: 
    if i in b:
        nn = a.index(i)
        mm = b.index(i)
        break




# 출력 

for i in range(m):
    if i == mm: print(a)
    else: print('.'*nn,b[i],'.'*(n-nn-1),sep='')
