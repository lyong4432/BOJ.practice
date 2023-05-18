s = list(map(int, input().split()))
wallet = 5000
change =  5000 - (s.count(1)*500 + s.count(2)*800 + s.count(3)*1000)

print(change)
