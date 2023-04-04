arr = []
while True:
    try:
        a,b,c = map(int, input().split())
        move1 = c-b-1
        move2 = b-a-1
        if move1>= move2:
            arr.append(move1)
        else:
            arr.append(move2)
    except EOFError:
        break

for i in arr:
    print(i)
