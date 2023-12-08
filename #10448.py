import sys 
input = sys.stdin.readline

N = [i*(i+1)//2 for i in range(1,46)]
def checkEureka(n):
    flag = 0
    for i in N: 
      for j in N: 
        for k in N: 
          if i + j + k == n: 
            flag = 1
    return flag
          
for _ in range(int(input())):
    n = int(input())
    print(checkEureka(n))
