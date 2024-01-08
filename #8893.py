import sys
from itertools import permutations
input = sys.stdin.readline

    
for _ in range(int(input())):
    P = []
    words = []
    for i in range(int(input())):
        s = input().strip()
        words.append(s)

    nCr = list(permutations(words,2))
    
    for i in nCr: 
        s1 = i[0]+i[1]
        l = len(s1)
        if l %2 == 0: 
            if s1[:l//2] == s1[l//2:][::-1]: 
                P.append(s1)

        else: 
            if s1[:l//2] == s1[l//2+1:][::-1]: 
                P.append(s1)

            

    if len(P) == 0: print(0)
    else: print(P[0])
