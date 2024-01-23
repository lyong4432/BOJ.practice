import sys 
input = sys.stdin.readline  
sys.setrecursionlimit(10000)
n = int(input())

def isPrime(num):
    for i in range(2, int(num/2+1)):
        if num%i == 0: 
            return False
    return True

def DFS(num1):
    if len(str(num1)) == n:
        print(num1)
    else: 
        for i in range(1,10):
            if i %2 == 0: 
                continue
            if isPrime(num1 * 10 +i):
                DFS(num1 * 10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)


# from 코딩테스트책 
