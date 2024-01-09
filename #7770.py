import sys
input = sys.stdin.readline

k = int(input())

floor = 1
n = 1
n1 = 1
while True: 
    n += (n1 + 4 * floor)

    n1 = n1 + 4 * floor
    if k - n >= 0: floor += 1
    else: break 

print(floor)
