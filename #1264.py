# 모음의 개수 출력 

vowels = ['a','e','i','o','u','A','E','I','O','U']
j = 0
array = []
while j == 0:
    st = input()
    count = 0
    if st =="#":
        j = 1
    else:    
        for i in st:
            if i in vowels:
                count+=1
        array.append(count)

for i in array:
    print(i)
