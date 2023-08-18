import sys
input = sys.stdin.readline

n, h, w = map(int, input().split())
word = ['']*n
for i in range(h):
    s = input().strip()
    c = 0
    for j in range(0,n):
        word[j] += s[c:c+w]
        c+= w

for i in word: 
    if i.count('?')== h*w:
        print('?',end='')
    else: 
        i = i.replace('?','')
        print(i[0],end='')
