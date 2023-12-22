import sys
input = sys.stdin.readline

r, c = map(int, input().split())
A, B = map(int, input().split())


for i in range(r * A):
    for j in range(c * B):  
        if ((i % (A*2)) < A) == ((j % (B*2)) < B): 
            print("X", end="")
        else:
            print(".", end="") 
    print("")
