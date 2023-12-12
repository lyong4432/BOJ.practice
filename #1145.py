import sys 
input = sys.stdin.readline

N = list(map(int, input().split()))
N.sort()
k = N[2]
while True: 
  cnt = 0
  for i in N:
    if k%i == 0:
      cnt += 1
  if cnt >= 3: 
    print(k)
    break
  else: k+= 1
