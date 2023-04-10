j=1
ans = []
while j == 1:
    n = input()
    answer = 0
    if n == '0':
        j = 0
    else:
        if len(n) == 1:
            ans.append(int(n))
        elif len(n) == 2:
            answer = int(n[0])*2 + int(n[1])
            ans.append(answer)
        elif len(n) == 3:
            answer = int(n[0])*3*2 + int(n[1])*2 + int(n[2])
            ans.append(answer)
        elif len(n) == 4:
            answer = int(n[0])*4*3*2 + int(n[1])*3*2 + int(n[2])*2 + int(n[3])
            ans.append(answer)
        elif len(n) == 5:
            answer = int(n[0])*5*4*3*2 + int(n[1])*4*3*2 + int(n[2])*3*2 + int(n[3])*2 + int(n[4])
            ans.append(answer)

for i in ans:
    print(i)
