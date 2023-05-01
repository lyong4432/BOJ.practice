imo = input()
leng = len(imo)
for i in imo:
    if i =='_':
        leng += 5
    elif i == ':':
        leng += 1

print(leng)
