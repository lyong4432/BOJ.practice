h1, m1, s1 = map(int,input().split(':'))
h2, m2, s2 = map(int,input().split(':'))
 
t1 = h1*3600+m1*60+s1
t2 = h2*3600+m2*60+s2
# 24시간이 넘어간 경우
if t1 > t2 : t = (t2-t1) % 86400
else: t = t2-t1
 

if t == 0 : print('24:00:00')
else:
    h = t // 3600
    m = t % 3600 // 60
    s = t % 3600 % 60
    print('%02d:%02d:%02d' % (h,m,s))

# 계속 틀린 문제라서 블로그 참고 
