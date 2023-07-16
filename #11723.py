import sys
input = sys.stdin.readline
arr = []
n = int(input().strip())
for i in range(n):
    ss = list(map(str, input().split()))
    if ss[0] == 'add':
        if ss[1] not in arr:
            arr.append(ss[1])
    elif ss[0] == 'remove':
        if ss[1] in arr:
            arr.remove(ss[1])
    elif ss[0] == 'check':
        if ss[1] in arr: print(1)
        else: print(0)
    elif ss[0] == 'toggle':
        if ss[1] in arr: arr.remove(ss[1])
        else: arr.append(ss[1])
    elif ss[0] == 'all':
        arr.clear()
        arr = ['1','2','3','4','5','6','7',\
               '8','9','10','11','12','13','14','15','16','17','18','19','20']
    elif ss[0] == 'empty': arr.clear()
