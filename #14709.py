import sys
input = sys.stdin.readline
res= [0,0,0,0]
n = int(input().strip())
for i in range(n):
    a= list(map(int, input().split()))
    a.sort()
    if a == [1,3]: res[0] = 1
    elif a == [1,4] : res[1] = 1
    elif a == [3,4] : res[2] = 1
    
    if 2 not in a and 5 not in a: 
        res[3] += 1
    
if res == [1,1,1,n]:
    print('Wa-pa-pa-pa-pa-pa-pow!')
else: 
    print('Woof-meow-tweet-squeek')
