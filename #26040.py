s = input()
b = list(map(str, input().split()))
answer = ''
for i in s:
    if i in b:
        answer += i.lower()
    else:
        answer += i

print(answer)
