n = int(input())
score = list(map(int, input().split()))
m = max(score)
hap = 0
for i in score:
    hap += i / m * 100

print(hap/len(score))

    
