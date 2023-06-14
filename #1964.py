n = int(input())
# 5 12 15 
dot = 1
if n == 1:
    dot += 4
else: 
    for i in range(1,n+1):
        dot +=  4 + (i-1)*3

print(dot%45678) 
