import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
N = [i for i in range(1,n+1)]

i = 0
c = 0
print('<',end='')
while len(N) != 0: 
    c += 1
    if len(N) == i: 
        i = 0

    if c == k: 
        if len(N) != 1:
            print(f'{N.pop(i)},',end=' ')
        else: print(f'{N.pop(i)}',end='')
        c = 0
    else:
        i += 1
print('>')

#PyPy3로 맞춤
