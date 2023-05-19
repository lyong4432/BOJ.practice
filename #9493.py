j = 1
res = []

while j == 1:
    m,a,b = map(int, input().split())
    if m == 0 and a == 0 and b == 0:
        j = 2
    else:
        time = m/(a/3600) - m/(b/3600)
        h = time//3600
        mm = (time%3600)//60
        ss = round((time%3600)%60)
        res.append('%d:%02d:%02d'%(h,mm,ss))

for i in res:
    print(i)
