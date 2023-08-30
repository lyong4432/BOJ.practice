import sys 
input = sys.stdin.readline
k = int(input().strip())
cnt = 0
for _ in range(k):
    s = list(map(str, input().strip().split('.')))
    
    if len(s) == 2:
        if ' ' not in s[0] and 1<=len(s[0]) <=8 and 1<=len(s[1]) <=3 and s[0]!='': 
            cnt += 1

print(cnt)
