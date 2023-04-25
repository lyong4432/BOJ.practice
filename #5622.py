two = ['A','B','C']
thr = ['D','E','F']
four = ['G','H','I']
five = ['J','K','L']
six = ['M','N','O']
sev = ['P','Q','R','S']
eig = ['T','U','V']
nin = ['W','X','Y','Z']

n = input()
hap = 0
for i in n:
    if i in two:
        hap +=3
    elif i in thr:
        hap +=4
    elif i in four:
        hap +=5
    elif i in five:
        hap += 6
    elif i in six:
        hap += 7
    elif i in sev:
        hap += 8
    elif i in eig:
        hap += 9 
    elif i in nin:
        hap += 10

print(hap)
