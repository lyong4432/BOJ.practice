import sys
input = sys.stdin.readline
n = int(input().strip())
word_game = []
for i in range(n):
    word_game.append(input().strip())
answer = ''
unknown = word_game.index('?')

m = int(input().strip())

if n == 1 and m == 1:
    answer = input().strip()

elif m >= 2:
    for i in range(m):
        guess = input().strip()
        if guess not in word_game:
            if unknown == 0: 
                unknownNext = word_game[unknown+1]
                if guess[-1] == unknownNext[0]:
                    answer = guess
            elif unknown == n-1:
                unknownPre = word_game[unknown-1]
                if guess[0] == unknownPre[-1]:
                    answer = guess
            else: 
                unknownPre = word_game[unknown-1]
                unknownNext = word_game[unknown+1]
                if guess[-1] == unknownNext[0] and guess[0] == unknownPre[-1]:
                    answer = guess




    
print(answer)
