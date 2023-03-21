# 5개 수를 입력받아서 더한 후 출력하는 코드

array = []
sum = 0
for i in range(1,6):
    num = int(input())
    array.append(num)

for i in array:
    sum+=i

print(sum)
