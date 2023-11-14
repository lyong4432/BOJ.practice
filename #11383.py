n,m = map(int, input().split())
N = []
def Double(arr):
    result =''
    for i in arr:
        result += i*2
    return result

for i in range(n):
    a = input()
    a = list(a)
    N.append(Double(a))
f = 1
for i in range(n):
    a = input()
    if a != N[i]: 
        f = 0
        break

if f == 1: print('Eyfa')
else : print('Not Eyfa')
