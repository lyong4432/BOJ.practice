n,k = map(int, input().split())
N =[]
for i in range(n):
    a = int(input())
    N.append(a)
N.reverse()
cnt = 0
for i in N:
    cnt += k//i
    k = k%i

print(cnt)
