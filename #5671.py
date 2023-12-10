import sys
input = sys.stdin.readline

while True: 
    try:
        a,b = map(int, input().split())
        cnt = 0 
        for i in range(a,b+1):
            i = str(i)
            flag = 1
            for j in range(10): 
                if i.count(f'{j}') > 1: 
                    flag = 0
                    break
            if flag == 1: 
                cnt += 1 
        print(cnt)
    except EOFError: break 
