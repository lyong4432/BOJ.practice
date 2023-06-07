cam = ['C','A','M','B','R','I','D','G','E']

n = input()
nn = ''
for i in n:
    if i not in cam:
        nn += i

print(nn)
