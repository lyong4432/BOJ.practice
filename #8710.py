import math
k, w, m = map(int, input().split())

cha = w - k 

if cha<=0:
    print(0)
else: 
    print(math.ceil(cha/m))
