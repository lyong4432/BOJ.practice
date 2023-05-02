a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

if t<=30:
    print(f'{a} {b}')
elif t<=45:
    print(f'{a+((t-30)*x)*21} {b}')
else:
    print(f'{a+((t-30)*x)*21} {b+((t-45)*y)*21}')
