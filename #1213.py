import sys
input = sys.stdin.readline
s = input().strip()
s = list(s)
set_s = list(set(s))
set_s.sort()

cnt = 0
hole = ''
for i in set_s: 
    if s.count(i)%2 != 0: 
        cnt += 1
        hole = i
    if cnt > 1: 
        break
    
result = ''
if hole != '':
    s.pop(s.index(hole))
if cnt > 1 : print('I\'m Sorry Hansoo')
else: 
    for i in set_s:
        result += i * (s.count(i)//2)
    result += hole 
    for i in set_s[::-1]:
        result += i * (s.count(i)//2)
    print(result)
