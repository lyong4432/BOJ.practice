import sys 
input = sys.stdin.readline  

n, a, b = map(int, input().split())

if a < b: 
    print('Bus')
elif a > b: 
    if n <= b: print('Subway')
    else: print('Bus')
else: print('Anything')
