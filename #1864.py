res = []
dic = {'-':0,'\\':1,'(':2,'@':3,'?':4,'>':5,'&':6,'%':7,'/': -1}
while True:
    s = input()
    if s == '#':
        break
    else: 
        ans = 0
        s = s[::-1]

        for i in range(len(s)-1,-1,-1):
            ans += (8**i)*dic[s[i]]
          
        res.append(ans)

for i in res: print(i)
