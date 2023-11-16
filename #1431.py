import sys 
input = sys.stdin.readline
N = {}
for i in range(int(input().strip())):
    s = input().strip()
    leng = len(s)
    cnt = 0
    for j in s: 
        if j.isdigit():
            cnt += int(j)
    N[s] = [leng,cnt]

N = dict(sorted(N.items(), key=lambda x: x[0]))
N = dict(sorted(N.items(), key=lambda x: x[1][1]))
N = dict(sorted(N.items(), key=lambda x: x[1][0]))
print(*N.keys(),sep='\n')
