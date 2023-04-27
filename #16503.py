a,b,c,d,e = map(str, input().split())
a = int(a)
c = int(c)
e = int(e)
res = []

def buho(i,j,bu):
    if bu == '+':
        return i + j
    elif bu == '-':
        return i - j
    elif bu == '*':
        return i * j
    elif bu == '/':
        return int(i / j)

# 1 
one = buho(a,c,b)
two = buho(one,e,d)
res.append(two)

# 2
one = buho(c,e,d)
two = buho(a,one,b)
res.append(two)

res.sort()

for i in res:
    print(i)

