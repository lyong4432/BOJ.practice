import sys


input = sys.stdin.readline
n = int(input().strip())
unit = [500,100,50,10,5,1]
change = 1000-n
cnt = 0

for i in unit:
    cnt += change//i
    change %= i
    
print(cnt)


