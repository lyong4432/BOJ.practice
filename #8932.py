import sys 
input = sys.stdin.readline
n = int(input().strip())
S = [[9.23076,26.7, 1.835],
     [1.84523, 75, 1.348],
     [56.0211, 1.5, 1.05],
     [4.99087, 42.5, 1.81],
     [0.188807, 210, 1.41],
     [15.9803, 3.8, 1.04],
     [0.11193, 254, 1.88]
     ]

def getScore(scores):
    hap = 0
    for i,j in enumerate(scores): 
        if i%3==0: 
            hap += int(S[i][0] * (S[i][1]-j)**S[i][2])
        else: 
            hap += int(S[i][0] * (j-S[i][1])**S[i][2])
    return hap
for i in range(n):
    scores = list(map(int,input().split()))
    print(getScore(scores))
