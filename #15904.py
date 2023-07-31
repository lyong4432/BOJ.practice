import sys
input = sys.stdin.readline
s = input().strip()
original = 'UCPC'

j = 0
for i in s: 
    if i == original[j]: 
        j += 1
    if j == 4: break



if j == 4: 
    print('I love UCPC')
else: print('I hate UCPC')
