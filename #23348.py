import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
n = int(input().strip())
res = []
for i in range(n):
    hap = 0
    for j in range(3):
        a1,b1,c1 = map(int, input().split())
        hap += a*a1+b*b1+c*c1
    

    res.append(hap)

res.sort(reverse=True)

print(int(res[0]))
