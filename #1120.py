import sys
input = sys.stdin.readline
a, b = map(str,input().split())

if len(a) == len(b):
    cnt = 0
    for i in range(len(b)):
        if a[i] != b[i]: cnt += 1
    print(cnt)
else: 
    res = []
    for i in range(len(b)- (len(a)-1)):
        new = b[i:i+len(a)]
        cnt = 0
        
        for j in range(len(new)):
            if a[j] != new[j]: cnt +=1
        res.append(cnt)
    
    res.sort()
    print(res[0])





