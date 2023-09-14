import sys
input = sys.stdin.readline
num = 1000001
arr = [True for _ in range(num)]
for i in range(2, int((num-1)**0.5)+1):
    if arr[i]:
        for k in range(i+i, num, i):
            arr[k] = False

while True:
    n = int(input().strip())

    if n == 0:
        break

    f = 0

    for i in range(3, n//2+1):
        if arr[i] and arr[n-i]:
            print(str(n) + " = " + str(i) + " + " + str(n-i))
            f = 1
            break
    if f== 0:
        print("Goldbach's conjecture is wrong.")


#pypy3로 제출하니까 시간초과 안 남.. 
