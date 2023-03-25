# 비밀번호는 6자리 이상, 9자리 이하 
# 입력한 것이 비밀번호로 사용가능한지 

n = int(input())
answer = []

for i in range(0,n):
    s = input()
    if len(s) >= 6 and len(s) <=9:
        answer.append('yes')
    else: 
        answer.append('no')

for i in answer:
    print(i)
