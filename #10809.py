# 97~122
alpha = [-1]*26
n = input()
for i in n:
    alpha[ord(i)-97] = n.index(i)

for i in alpha:
    print(i, end= ' ')


    
