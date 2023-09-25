yy1, mm1, dd1 = map(int, input().split())
yy2, mm2, dd2 = map(int, input().split())

years = yy2-yy1-1
if mm1 < mm2: years += 1
elif mm1 == mm2: 
    if dd1 <=dd2: years += 1
print(years)
print(yy2-yy1+1) 
print(yy2-yy1)
