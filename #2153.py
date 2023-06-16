n = input()
# 아스키 코드 영어 대문자 65~90
# 영어 소문자 97~122
hap = 0
for i in n:
    if i.isupper():
        hap += ord(i)-38
    else: 
        hap += ord(i)-96
cnt = 0
for i in range(2,hap):
    if hap%i==0:
        cnt += 1
        print('It is not a prime word.')
        break
if cnt == 0:    
    print('It is a prime word.')
