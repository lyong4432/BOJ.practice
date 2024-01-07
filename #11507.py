import sys
input = sys.stdin.readline

s = input().strip()
p, k, h, t = 13, 13, 13, 13
cards = []
for i in range(0,len(s),3):
    cards.append(s[i:i+3])
checked = []
# print(cards)
flag = 1
for i in cards: 
    if i in checked: 
        flag = 0
        break
    else:
        checked.append(i)

    if i[0] == 'H': h -=1
    elif i[0] == 'P': p -=1
    elif i[0] == 'T': t -=1
    elif i[0] == 'K': k -=1

if flag == 0: print('GRESKA')   
else: 
    print(p, k, h, t)
