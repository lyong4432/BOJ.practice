import sys
input = sys.stdin.readline

n = int(input())
f = int(input())
new = int(str(n)[:-2] +'00')

while True:
    if new % f == 0: 
        print(str(new)[-2:])
        break
    else: 
        new += 1
