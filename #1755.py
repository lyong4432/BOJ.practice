import sys

input = sys.stdin.readline
num = {}
m, n = map(int, input().split())
integer = ['zero','one','two','three','four','five','six','seven','eight','nine']
def convert(k):
    l = len(str(k))
    if l == 1: return integer[k]
    elif l == 2: return integer[k//10] + integer[k%10]




for i in range(m,n+1):
    num[i] = convert(i)


num = dict(sorted(num.items(), key=lambda x: x[1]))

cnt = 0
for i in num.keys():
    print(i,end = ' ')
    cnt +=1
    if cnt %10 == 0: print()
