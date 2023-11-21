# 큐 사용
from collections import deque 
import sys 
input = sys.stdin.readline
n = int(input().strip())
q = deque()
q = deque(range(1,n+1))

while len(q)!= 1 :
    q.popleft()
    q.append(q.popleft())
print(q.popleft())
