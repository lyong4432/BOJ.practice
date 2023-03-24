# counting vowels

n = int(input())
s = input()
vowels = [ 'a' ,'i' , 'u' , 'e', 'o']
answer = 0
for i in s:
    if i in vowels:
        answer+=1

print(answer)
