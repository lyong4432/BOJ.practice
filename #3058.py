n = int(input())
answer = []

for _ in range(n):
    a = list(map(int, input().split()))
    hap = 0
    arr = []
    for i in a:
        if i%2 == 0:
            arr.append(i)
    answer.append('%d %d'%(sum(arr),min(arr)))

for i in answer:
    print(i)
