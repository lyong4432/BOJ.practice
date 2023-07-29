import sys
top = ["`","1","2","3","4","5","6","7","8","9","0","-","="]
up = ["Q","W","E","R","T","Y","U","I","O","P","[","]","\\"]
mid = ["A","S","D","F","G","H","J","K",'L',";","'"]
bottom = ["Z","X","C","V","B","N","M",",",".","/"]

s = sys.stdin.readlines()
word = ''
for i in s:
    word += i[:-1]
    word += "+"

new = ''
for i in word[:-1]:
    if i in top: 
        new += top[top.index(i)-1]
    elif i in up: 
        new += up[up.index(i)-1]
    elif i in mid: 
        new += mid[mid.index(i)-1]
    elif i in bottom: 
        new += bottom[bottom.index(i)-1]
    elif i ==' ':
        new += ' '
    elif i == '+':
        new += "\n"
  
print(new)
