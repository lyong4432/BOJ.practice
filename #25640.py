# mbti 같은 사람의 수 출력

mb = input()
n = int(input())
sum = 0

for i in range(0,n):
    a = input()
    if a == mb:
        sum += 1

print(sum)
