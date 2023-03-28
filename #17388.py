# 세 학교의 점수가 100 이상이면 OK, 아니면 가장 낮은 점수의 학교이름을 출력

s, k, h = map(int, input().split())
num = {s: 'Soongsil', k : 'Korea', h:'Hanyang'}
if s + k + h >= 100:
    print('OK')
else: 
    print(num[min(num)])
