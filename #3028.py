import sys

input = sys.stdin.readline

cups = ['o','x','x']
s = input().strip()

for i in s: 
    if i == 'A':
        cups[0],cups[1] = cups[1],cups[0]
    elif i == 'B':
        cups[1],cups[2] = cups[2],cups[1]
    elif i == 'C':
        cups[0],cups[2] = cups[2],cups[0]

print(cups.index('o')+1)
