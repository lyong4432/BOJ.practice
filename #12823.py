import sys


whole = ''
hap =0

while True:
    try:
        a = input()
        whole += a
    except EOFError:
        break

N = whole.split(',')

for i in N:
    hap += int(i)

print(hap)
