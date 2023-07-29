
while True: 
    n = int(input())
    if n == 0: break
    max1 = 0
    name = ''
    for i in range(n):
        n, height = map(str, input().split())
        height = float(height)
        if max1 < height: 
            max1 = height
            name = n
        elif max1 == height: 
            name += f' {n}'
    print(name)
