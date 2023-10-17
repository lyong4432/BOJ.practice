import sys

input = sys.stdin.readline

for i in range(int(input().strip())):
    n,d,a,b,f = map(float, input().split())
    n = int(n)
    p = d/(a+b)*f
    print("%d %.6f"%(n,p))


# 거리 = 속력 * 시간 

# 시간 = 거리/속력 = d/(a+b)
# 파리의 이동거리 = f(파리의 속력) * 시간 = f * d/(a+b)


