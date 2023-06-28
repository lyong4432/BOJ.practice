n, l, d = map(int, input().split())
# n 앨범 수록곡 / l 모든 노래 길이 / 노래와 노래 사이 5초 
# 전화벨 d초에 한번 
time = 0
while time < n *(l+5):
    time += d
    if time%(l+5) >= l: break

print(time)
