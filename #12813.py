a = input()
b = input()
aandb = ''
aorb = ''
axorb =''
nota = ''
notb = ''
for i in range(len(a)):
    if a[i] == b[i] == '1': 
        aandb += '1'
        aorb += '1'
        axorb += '0'
    elif a[i] == b[i] == '0': 
        aandb += '0'
        aorb += '0'
        axorb += '0'
    elif a[i] != b[i]:
        aandb += '0' 
        aorb += '1'
        axorb += '1'
    if a[i] == '1': nota += '0'
    else: nota += '1'
    if b[i] == '1': notb += '0'
    else: notb += '1'
    
print(aandb)
print(aorb)
print(axorb)
print(nota)
print(notb)
