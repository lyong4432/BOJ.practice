# 영수증에서 총금액 x과 각 물건들의 금액의 합이 같은지 확인하는 문제 

x = int(input())
n = int(input())
sum = []
answer = 0

for i in range(0,n):
    a, b = map(int, input().split())
    sum.append(a*b)

for i in sum:
    answer+=i

if answer == x: 
    print('Yes')
else: 
    print('No')
