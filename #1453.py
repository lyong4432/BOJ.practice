n = int(input())
cnt = 0
peoples = list(map(int, input().split()))
people_set = set(peoples)

for i in people_set:
    if peoples.count(i)>=2:
        cnt += peoples.count(i)-1

print(cnt)
