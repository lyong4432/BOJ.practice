import sys
input = sys.stdin.readline
n = int(input().strip())

def n_number(n,i):
    n_num = ''
    while n:
        n_num = str(n%i) + n_num
        n//=i
    
    return n_num
cnt = 0
for i in range(2,10):
    a = n_number(n,i)
    if a == a[::-1]:
        print(i, a)
        cnt += 1

n = str(n)
if n == n[::-1]:
    print(10,n)
    cnt += 1

if cnt == 0: print('NIE')
