n = int(input())
prices = []
for i in range(n):
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    set_a = set(a)
    if len(set_a) == 1:
        prices.append(50000 + a[0]*5000)
    elif len(set_a) == 2:
        cnt = 0
        cnt1 = []
        for i in set_a:
            if a.count(i) == 3:
                prices.append(10000 + i*1000)
                break
            elif a.count(i) == 2:
                cnt +=1
                cnt1.append(i)
        if cnt == 1:
            prices.append(1000+cnt1[0]*100)
        elif cnt == 2:
            prices.append(2000+cnt1[0]*500+cnt1[1]*500)
    elif len(set_a) == 3:
        for i in set_a:
            if a.count(i) == 2:
                prices.append(1000+i*100)
                break
    else: 
        prices.append(a[0]*100)

prices.sort(reverse=True)
print(prices[0]) 


