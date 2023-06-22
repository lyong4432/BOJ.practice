n = int(input())
i = 0
while n >= (9**i):
    if n >= (9**i):
        i += 1
    else: break

for j in range(i-1,-1,-1):
    print(n//(9**j),end='')
    n %= 9**j
