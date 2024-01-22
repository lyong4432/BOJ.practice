import sys 
input = sys.stdin.readline  
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(v): 
    visited[v] = True
    for i in A[v]:
        if not visited[i]: DFS(i)

for i in range(m):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        DFS(i)

print(cnt)

# from 코테책이요... 
