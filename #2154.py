import sys
input = sys.stdin.readline
n = int(input().strip())


num = ''

for i in range(1,n+1):
    num += str(i)
    
print(num.find(str(n))+1)
