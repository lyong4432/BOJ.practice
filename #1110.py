n = int(input())

new = (n//10 + n%10)%10 + (n%10)*10
i = 1
while new != n:
    new = (new//10 + new%10)%10 + (new%10)*10
    
    i+= 1

print(i)
