n, b = map(int, input().split())
new = ''
while True: 
    if n%b >9:
        new += chr((n%b)+55)
    else:
        new += str(n%b)
    n //=b
    if n == 0: break

print(new[::-1])
