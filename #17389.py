n = int(input())
s = input().strip()
s = s.upper()
score = 0
bonus = 0

for i,jum in enumerate(s): 
    if jum == "O":
        score += i+1 + bonus
        bonus += 1
    else: 
        bonus = 0


print(score)
