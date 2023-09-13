import sys
input = sys.stdin.readline

while True:
    try: 
        n = int(input().strip())

    except: break

    cnt = 1
    one = 1
    while True:
        if one % n != 0:
            one = one*10 + 1
            cnt += 1
        else: 
            break
    print(cnt)
