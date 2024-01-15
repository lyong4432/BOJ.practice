chkList = [0]*4
myList = [0]*4
chkSecret = 0

def myadd(c):
    global chkList, myList, chkSecret

    if c == 'A': 
        myList[0] += 1
        if myList[0] == chkList[0]: chkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == chkList[1]: chkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == chkList[2]: chkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == chkList[3]: chkSecret += 1

def myremove(c):
    global chkList, myList, chkSecret

    if c == 'A': 
        if myList[0] == chkList[0]: chkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == chkList[1]: chkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == chkList[2]: chkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == chkList[3]: chkSecret -= 1
        myList[3] -= 1   


s, p = map(int, input().split())
result = 0
A = list(input())
chkList = list(map(int, input().split()))

for i in range(4):
    if chkList[i] == 0: chkSecret += 1

for i in range(p):
    myadd(A[i])

if chkSecret == 4: result += 1

for i in range(p,s):
    j = i - p
    myadd(A[i])
    myremove(A[j])
    if chkSecret == 4: result += 1

print(result)
