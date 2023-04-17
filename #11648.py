n = input()
step = 0
while len(n) >1:
    j = 1
    for i in n:
        j *= int(i)
    n = str(j)    
    step += 1

print(step)
