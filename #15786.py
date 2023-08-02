n, m = map(int, input().split())
origin = input()
for i in range(m):
    guess = input()
    idx = 0
    for i in guess:
        if i == origin[idx]:
            idx += 1
            if idx == n: break
        
    if idx == n: print('true')
    else: print('false')
