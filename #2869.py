import sys
import math
input = sys.stdin.readline

a,b,v = map(int, input().split())
print(math.ceil((v-b)/(a-b)))
# 올라가야 할 거리 : v-b
# 하루에 올라갈 수 있는 거리 : a-b
