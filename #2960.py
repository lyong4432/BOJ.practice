import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
N = [i for i in range(2,n+1)]

deleted = []
i = 0
while i < n-1:
    if N[i] in deleted: i += 1
    else: 
        for j in range(i,len(N),N[i]):
            if N[j] not in deleted: 
                deleted.append(N[j])
print(deleted[k-1])
