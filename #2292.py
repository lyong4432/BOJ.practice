n = int(input())
# 중간 1
# 1번째 2~7 6개 
# 2번째 8~19 12
# 3번째 20~37 18   

cnt = 1
i = 1
n -= 1
while True:
    if n <= 0: break
    else:
        n -= 6*i
        i += 1
        
        cnt += 1

print(cnt)
