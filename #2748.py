n = int(input())
hap = 0
n1 = 0 
n2 = 1
if n == 1:
    hap = 1
if n >= 2:
    for i in range(1,n):
        hap = n1+ n2
        n1 = n2
        n2 = hap

print(hap)
