n, x = map(int, input().split())
list_n = list(map(int, input().split()))
sound = x
j = 1
result = 1
while j == 1:
    for i in list_n:
        if sound > i:
            result = list_n.index(i)+ 1
            j = 2
            break
        sound += 1

print(result)
