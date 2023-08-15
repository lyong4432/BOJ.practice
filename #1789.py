import sys
input = sys.stdin.readline
cnt = 1
n = int(input().strip())
hap = 0
while True: 
    if hap >= n :
        break
    hap += cnt
    cnt += 1
if hap == n : print(cnt-1)
else: print(cnt-2)
