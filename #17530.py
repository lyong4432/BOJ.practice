a = int(input())
b = []

for i in range(a):
    b.append(int(input()))

if b[0] == max(b):
    print("S")
else:
    print("N")
