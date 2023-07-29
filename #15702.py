import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_score = list(map(int, input().split()))
max_score = 0
max_person = 100000
for _ in range(m):
    test = list(map(str, input().split()))
    score = 0
    test[0] = int(test[0])

    for j,k in enumerate(test[1:]):
        if k == 'O':
            score += n_score[j]

    if score > max_score:
        max_score = score
        max_person = test[0]
    elif score == max_score: 
        if max_person > test[0]:
            max_person = test[0]

print(max_person,max_score) 
