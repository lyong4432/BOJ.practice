n = int(input())
t = sorted(list(map(int, input().split())))
for k in range(n,-1,-1):
  if k <= t[-k]:
    print(k)
    break


"""----------------------------------
오늘 문제들 죄다 어려운 것만 골랐다.. 
내가 작성한 틀린 코드 
n = int(input())
quote = list(map(int, input().split()))
quote.sort()

# k번 이상이 k편이상 
# n - k 편이 k번 이하 
for i in quote:
    k = i
    cnt_up1, cnt_down1 = 0, 0
    cnt_up2 , cnt_down2 = 0, 0
    for j in quote:
        if k <= j:
            cnt_up1 += 1
        else:
            cnt_down1 += 1
        if k < j :
            cnt_up2 += 1
        else: cnt_down2 += 1
            
            
    if k == cnt_up1 and (n-k) == cnt_down1 : 
        print(k)
        break
    if k == cnt_up2 and (n-k) == cnt_down2 : 
        print(k)
        break



"""
