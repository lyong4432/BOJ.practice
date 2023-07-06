import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    word = input()
    word = word.lower()

    result = ''
    for i in range(97,123):
        if chr(i) not in word:
            result += chr(i)

    if len(result) == 0:
        print('pangram')
    else: print('missing',result)
