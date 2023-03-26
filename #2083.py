# age > 17 or weight >= 80 -> Senior, else -> Junior

array = []
j = 0
while j == 0:
    name, age, weight = map(str, input().split())
    if name =="#":
        j = 1
    else:    
        if int(age) > 17 or int(weight) >= 80:
            array.append(name+ ' Senior')
        else: 
            array.append(name+ ' Junior')

for i in array:
    print(i)
