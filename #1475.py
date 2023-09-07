import sys
input = sys.stdin.readline

n = input().strip()
chk = [0]*9

for i in range(9):
    chk[i] = n.count(str(i))
chk[6] += n.count('9')

if chk[6] % 2 == 1:
    chk[6] = chk[6]//2 + 1
else: 
     chk[6] = chk[6]//2

print(max(chk))
