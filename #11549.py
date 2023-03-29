t = int(input())
a = list(map(int, input().split()))
answer = 0

for i in a:
    if i == t:
        answer += 1

print(answer)
