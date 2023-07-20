t = int(input())
res = []
for _ in range(t):
    n = int(input()) 
    max = int(input())
    cnt = 0
    idx = 1
    whole = max
    for i in range(n-1):
        a = int(input())
        if max < a:
            max = a
            idx = i + 2
            cnt = 0
        elif max == a:
            cnt += 1
        whole += a
    if cnt >= 1: res.append('no winner')
    elif max/whole > 0.5: res.append(f'majority winner {idx}')
    else: res.append(f'minority winner {idx}')

for i in res: print(i)

# 어려워. 5트 ㅠㅅㅠ
