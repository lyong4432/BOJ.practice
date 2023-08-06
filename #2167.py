import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    nums=list(map(int, input().split()))
    arr.append(nums)
k = int(input().strip())
for _ in range(k):
    i,j,x,y = map(int, input().split())
    hap = 0
    for a in range(i-1,x):
        for b in range(j-1,y):
            hap += arr[a][b]
    print(hap)

# 다른 파이썬 풀이 보면 누적합으로 구했던데 아직 몰라서 pypy3로 제출함
