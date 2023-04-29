s = int(input())
a = int(input())
b = int(input())

n = a
cnt = 0

while s > n:
    if s>n:
        n += b
        cnt += 1

print(250 + cnt*100)
