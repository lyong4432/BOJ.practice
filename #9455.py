import sys

input = sys.stdin.readline
for _ in range(int(input())):
    m, n = map(int, input().split())
    boxes = []
    for i in range(m):
        arr = list(map(int, input().split()))
        boxes.append(arr)

    result = 0
    for i in range(n):
        cnt = 0
        for j in range(m-1,-1,-1):
            if boxes[j][i] == 1: 
                cnt += 1
                result += (m-j) - cnt
                
    print(result)
