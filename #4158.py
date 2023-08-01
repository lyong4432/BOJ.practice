import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break

    sun = set()
    san = set()

    for i in range(n):
        san.add(int(input().strip()))
    for i in range(m):
        sun.add(int(input().strip()))

    common_elements = san.intersection(sun)
    cnt = len(common_elements)
   
    print(cnt)
