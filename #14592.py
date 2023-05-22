n = int(input())

maxS = 0
minC = 50
minL = 179
result = 0

for i in range(1,n+1):
    s, c, l = map(int, input().split())

    if s > maxS:
        maxS = s
        minC = c
        minL = l
        result = i
    elif s == maxS:
        if minC > c:
            minC = c
            minL = l
            result = i
             
        elif minC == c:
            if minL > l:
                minL = l
                result = i

print(result)
