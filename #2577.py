a = int(input())
b = int(input())
c = int(input())
hap = str(a * b * c)
ans = [0]*10

for i in hap:
    for j in range(0,10):
        if i == f'{j}':
           ans[j] += 1
        
for i in ans:
    print(i)   
