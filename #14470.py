

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
temp = a
time = 0

if a < 0:
    time += (-1)*temp*c
    time += d
    time += b*e
elif a > 0:
    time = (b-a)*e
print(time)
