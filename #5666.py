res = []
while True:
    try:
        h,p = map(int, input().split())
        res.append(f'{h/p:.2f}')
    except EOFError:
        break
        

for i in res:
    print(i)
