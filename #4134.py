import sys

input = sys.stdin.readline

def prime(x):
    if x==0 or x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
n = int(input().strip())
for i in range(n):
    x = int(input().strip())
    while True:
        if(prime(x)):
            print(x)
            break
        x+=1
