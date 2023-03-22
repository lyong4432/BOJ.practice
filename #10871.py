# n, x를 입력 받아서 숫자 n개를 받고, x보다 작은 수를 출력하기 

n, x = map(int, input().split())
a= list (map(int, input().split()))
answer = []
for i in a: 
    if x>i:
        answer.append(i)

for i in answer:
    print(i, end =' ')
