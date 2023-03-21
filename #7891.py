# 처음에 정수 n을 받아서 2개의 정수 n쌍을 입력받는다. 
# 출력으로는 2개의 정수합 n쌍을 출력한다.

num1 = int(input())
sum_array = []
for i in range(1,num1+1):
    a , b = map(int, input().split())
    sum_array.append(a+b)

for i in sum_array:
    print(i)
