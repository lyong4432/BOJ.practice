import sys
input = sys.stdin.readline
n = int(input().strip())
name = {}
for i in range(n):
    a, b = map(str, input().split())
    if b == 'enter':
        name[a] = 1
    elif b == 'leave':
        del name[a]
    
sortec_name = dict(sorted(name.items(),reverse=True))

print(*sortec_name.keys(),sep='\n')
