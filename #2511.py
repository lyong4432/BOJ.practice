A = list(map(int, input().split()))
B = list(map(int, input().split()))
a, b = 0, 0
result = ''
for i in range(10):
    if A[i] > B[i]:
        a += 3
        result='A'
    elif A[i] < B[i]:
        b += 3
        result='B'
    else: 
        a += 1
        b += 1

print(a,b)
if a > b: print('A')
elif a < b: print('B')
else: 
    if result == 'A': print('A')
    elif result == 'B': print('B')
    else: 
        print('D')
