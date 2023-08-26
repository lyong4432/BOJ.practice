import sys 
input = sys.stdin.readline
k = int(input().strip())
for _ in range(k):
    s = []
    v = []
    o = []
    ss = int(input().strip())
    vv = int(input().strip())
    oo = int(input().strip())
    for i in range(ss):
        s.append(input().strip())
    for i in range(vv):
        v.append(input().strip())
    for i in range(oo):
        o.append(input().strip())
   
    for i in s:
        for j in v:
            for l in o:
                print(f'{i} {j} {l}.')
    print()
