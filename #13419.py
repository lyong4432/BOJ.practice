import sys
input = sys.stdin.readline
n = int(input().strip())
for i in range(n):
    a = input().strip()
    if len(a) % 2 != 0:
        a = a * 2
        
    for j in range(0,len(a),2):
        print(a[j],end='')
    print()
    for j in range(1,len(a),2):
        print(a[j],end='')
    print()
