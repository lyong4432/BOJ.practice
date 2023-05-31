y, m = map(int, input().split())
yy, mm = 0,0
if y == 0:
    mm = 15 * m 
elif y ==1:
    yy = 15
    mm = m * 9
elif y >=2:
    yy = 15 + 9 + (y-2) * 4 
    mm = m*4
yy += mm//12
mm = mm%12

print(f'{yy} {mm}')
