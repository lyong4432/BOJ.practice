import math 
a,b = map(int, input().split())
hap = 0

for i in range(a,b+1):
    j = round(math.sqrt(2*i))
   
    hap += j

print(hap)
