import sys
input = sys.stdin.readline

S = []
S1 = []
hap = 0
for i in range(10):
    n = int(input())
    hap += n
    S.append(hap)


S.reverse()
diff = 100
answer = 0
for i in S: 
    if abs(i-100) <diff:
        diff = abs(i-100)
        answer = i

print(answer)
