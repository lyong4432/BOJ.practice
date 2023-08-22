import sys

input = sys.stdin.readline
n = int(input().strip())
for i in range(n):
    t, num = map(str, input().split())
    res = ''
    if t == '1': 
        s = num.split('.')
        for j in s:
            j = int(j)
            a = bin(j)
            a = a[2:]
            a = '0'*(8-len(a)) + a
            res += a
        res = int(res,2)
    elif t == '2':
        num = int(num)
        s = bin(num)
        s = s[2:]
        s = '0'*(8*8-len(s)) + s
        for j in range(0,64,8):
            k = s[j:j+8]
            k = int(k,2)
            res += str(k)
            if j != 56: res += '.'
  print(res)



