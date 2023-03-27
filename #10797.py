# 차량 10부제; 날짜의 일의자리 = 차번호의 일의자리 -> 위반, 위반한 차량수 출력

date = int(input())
car = list(map(int, input().split()))
sum = 0 

for i in car:
    if date == i:
        sum += 1

print(sum)
