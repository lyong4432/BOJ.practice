n = int(input())
a = []
for i in range(n):
    d,f,p = map(float, input().split())
    a.append(f'${d*f*p:.2f}')

for i in a:
    print(i)
