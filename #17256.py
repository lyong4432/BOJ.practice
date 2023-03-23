# a 🍰 b = (a.z + b.x, a.y × b.y, a.x + b.z) = C
# 입력으로 ax, ay, az 와 cx, cy, cz가 주어진다. 

ax,ay,az = map(int, input().split())
cx, cy, cz = map(int, input().split())

print(cx - az, cy // ay, cz -ax)
