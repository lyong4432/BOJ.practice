import sys
input = sys.stdin.readline
n, k = map(int,input().split())
prime = []
for i in range(2,k):
    if n%i == 0: 
        print('BAD',i)
        break
else:
    print('GOOD')
