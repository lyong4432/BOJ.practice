# 0 < A, B <= 10 

n = input()

if len(n) == 4:
    a = int(n[0] + n[1])
    b = int(n[2] + n[3])
elif len(n) == 3:
    a = int(n[0] + n[1])
    b = int(n[2])
    if a > 10:
        a = int(n[0])
        b = int(n[1]+n[2])
else:
    a = int(n[0])
    b = int(n[1])

print(a+b)
