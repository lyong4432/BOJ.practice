import sys
input = sys.stdin.readline
cnt = 1
while True: 
    n = int(input().strip())
    if n == 0: break
    else: 
        songs =[]
        for i in range(n):
            songs.append(input().strip())
        songs.sort()
        print(cnt)
        for i in songs: print(i)
        cnt += 1
