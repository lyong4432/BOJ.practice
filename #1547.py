m = int(input())
ball = 1
for i in range(m):
    a,b = map(int, input().split())
    if a not in [1,2,3] or b not in [1,2,3]:
        print(-1)
        break
    else:
        if a == ball:
            ball = b
        elif b == ball:
            ball = a

print(ball)
