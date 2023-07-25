n = int(input())
s = input()

A = '000000'
B = '001111'
C = '010011'
D = '011100'
E = '100110'
F = '101001'
G = '110101'
H = '111010'
word = ''
k = 1
d = 0
words = ["A",'B','C','D','E','F','G','H']
j = 0
cnt = [0,0,0,0,0,0,0,0]
for i in s:
    
    if i == A[j]:
        cnt[0] += 1
    if i == B[j]:
        cnt[1] += 1
    if i == C[j]:
        cnt[2] += 1
    if i == D[j]:
        cnt[3] += 1
    if i == E[j]:
        cnt[4] += 1
    if i == F[j]:
        cnt[5] += 1
    if i == G[j]:
        cnt[6] += 1  
    if i == H[j]:
        cnt[7] += 1  
    
    
    j += 1
    if j == 6: 
        j = 0
        if max(cnt) >= 5:
            word += words[cnt.index(max(cnt))]
        else: 
            print(k)
            d = 1
            break
        cnt = [0,0,0,0,0,0,0,0]
        k += 1

if d == 0: print(word)


# 난잡해.. 시간이 된다면 다시 고쳐야겠다.
