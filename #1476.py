import sys
input = sys.stdin.readline
earth, sun, moon = map(int, input().split())
# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19

t = 0
e,s,m =0,0,0
while True:
    if earth == e and sun == s and moon == m:
        print(t)
        break
    else:
        e += 1
        s += 1
        m += 1
        t += 1
        if e == 16:
            e = 1
        if s == 29:
            s = 1
        if m == 20:
            m = 1
