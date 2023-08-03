# 맞았습니다.
n = int(input())
lst = list(map(int, input().split()))

temp = sum(lst)

answer = 0
for i in range(n-1):
    temp -= lst[i]
    answer += temp * lst[i]
  
print(answer)
