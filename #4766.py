j = 1
arr = []
ini = float(input())
while j ==1:
    n = float(input())
    if n == 999:
        j = 0
    else: 
        arr.append('%.2f'%(n - ini))
        ini = n

for i in arr:
    print(i)
