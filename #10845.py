import sys

input = sys.stdin.readline
n = int(input().strip())
Q = []
for i in range(n):
    commands = list(map(str, input().split()))
    if commands[0] == 'push':
        Q.append(commands[1])
    elif commands[0] == 'pop':
        if len(Q) == 0: print(-1)
        else: 
            print(Q[0])
            Q.pop(0)
    elif commands[0] == 'size': print(len(Q))
    elif commands[0] == 'empty': 
        if len(Q) == 0: print(1)
        else: print(0)
    elif commands[0] == 'front':
        if len(Q) == 0: print(-1)
        else: 
            print(Q[0])
    elif commands[0] == 'back':
        if len(Q) == 0: print(-1)
        else: 
            print(Q[-1])


