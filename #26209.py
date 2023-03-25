# 1바이트가 제대로 입력이 되었는지; 비트에 1, 0만 입력할 수 있음

n = list(map(int, input().split()))
answer = 'S'
for i in n: 
    if not(i == 0 or i ==1):
        answer = 'F'
        break

print(answer)
