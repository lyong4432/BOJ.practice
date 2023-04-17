n = int(input())
m = int(input())
tun = []
in_t = m
tun.append(in_t)
for i in range(n):
    a, b = map(int, input().split())
    in_t += (a - b)
    tun.append(in_t)

if min(tun)<0:
    print(0)
else:
    print(max(tun))
