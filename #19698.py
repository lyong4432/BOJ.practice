# 헛간의 넓이 : w * h, 소 한 마리당 필요한 넓이 : l * l, 헛간에 살고싶다고 응모한 소 : n 마리 

n, w, h, l = map(int, input().split())

cows = (w // l ) * (h // l)

if n >= cows:
    print(cows)
else: 
    print(n)
