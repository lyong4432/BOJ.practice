n = int(input())
m = int(input())
target = list(map(int, input().split()))
people = [0]*n
for i in range(m):
    guess = list(map(int, input().split()))
    for j in range(n):
        if guess[j] == target[i]:
            people[j] += 1

        if target[i] == j+1:
            people[j] += n-guess.count(target[i])

    
    

for i in people: print(i)
