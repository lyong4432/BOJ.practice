people = list(map(int, input().split()))
x,y,r = map(int, input().split())
cnt = 0 
for i,p in enumerate(people): 
    if x == p:
        print(i+1)
        cnt += 1

if cnt == 0: print(0)
