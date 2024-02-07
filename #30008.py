n, k = map(int, input().split())
grade = list(map(int, input().split()))


def check(p):
    if 0 <= p <= 4: return 1
    elif p <= 11: return 2
    elif p <= 23: return 3
    elif p <= 40: return 4
    elif p <= 60: return 5
    elif p <= 77: return 6
    elif p <= 89: return 7 
    elif p <= 96: return 8 
    elif p <= 100: return 9

for i in grade: 
    a = check(i * 100 // n)
    print(a, end=' ')
