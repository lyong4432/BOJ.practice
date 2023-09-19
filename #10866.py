import sys

input = sys.stdin.readline
n = int(input().strip())
D = []
for i in range(n):
    commands = list(map(str, input().split()))
    if commands[0] == 'push_front':
       D.insert(0,commands[1])
    elif commands[0] == 'push_back':
       D.append(commands[1])
    elif commands[0] == 'pop_front':
        if len(D) == 0: print(-1)
        else: 
            print(D[0])
            D.pop(0)
    elif commands[0] == 'pop_back':
        if len(D) == 0: print(-1)
        else: 
            print(D[-1])
            D.pop()
    elif commands[0] == 'size': print(len(D))
    elif commands[0] == 'empty': 
        if len(D) == 0: print(1)
        else: print(0)
    elif commands[0] == 'front':
        if len(D) == 0: print(-1)
        else: 
            print(D[0])
    elif commands[0] == 'back':
        if len(D) == 0: print(-1)
        else: 
            print(D[-1])


