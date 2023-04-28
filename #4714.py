j = 1
ans =[]
while j == 1:
    a = float(input())
    if a == -1.0:
        j =2
    else:
        ans.append(f'Objects weighing {a:.2f} on Earth will weigh {a*0.167:.2f} on the moon.')

for i in ans:
    print(i)
