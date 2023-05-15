n = int(input())
if n == 0:
    print('divide by zero') #divide 스펠링 실수로 잘못써서 많이 틀림.. ㅎㅋ
else:
    score = list(map(int, input().split()))
    print("1.00")
    
    
n = int(input())
if n == 0:
    print('divide by zero')
else:
    score = list(map(int, input().split()))
    aver = sum(score)/n
    score_ = set(score)
    expectation = 0
    for i in score_:
        expectation += i*score.count(i)/n
    else: print(f'{aver/expectation:.2f}')
