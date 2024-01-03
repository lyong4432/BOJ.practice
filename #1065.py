import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(1,n+1):
    if i <100: cnt += 1
    else: 
        k = list(str(i))
        dis = int(k[0]) - int(k[1])
        #print(k, dis)
        flag = 1
        for j in range(1,len(k)-1):
            if int(k[j])-int(k[j+1]) != dis:
                flag = 0
                break
        if flag: cnt += 1
print(cnt)
