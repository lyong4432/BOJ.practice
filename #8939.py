import sys
input = sys.stdin.readline
a, b = map(str, input().split())
hap = ''
lang = len(a)
if len(a) > len(b):
    lang = len(b)
    n = len(a)- len(b)
    hap += a[:n]
    a = a[n:]
elif len(a) < len(b):
    n = len(b) - len(a)
    hap += b[:n]
    b = b[n:]
for i in range(lang):
    k = int(a[i])+ int(b[i])
    hap += str(k)

print(hap)
