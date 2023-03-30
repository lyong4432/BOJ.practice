
alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

s = input()

for i in s:
    for j in range(0,26):
        if alp[j] == i :
            array[j] +=1

for i in array:
    print(i, end = ' ')
