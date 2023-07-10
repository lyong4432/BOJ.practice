n = int(input())
for i in range(n):
    words = list(map(str, input().split()))
    new =''
    for word in words: 
        new += word[::-1]
        new += ' '

    print(new)
