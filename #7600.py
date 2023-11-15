import sys 
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '#': break
    cnt = 0
    s = s.upper()
    for i in range(65,91):
        if chr(i) in s: cnt += 1
    print(cnt)
