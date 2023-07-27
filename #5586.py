s = input()

j , k = 0,0 
for i in range(len(s)-2):
    if s[i:i+3] == 'JOI': j += 1
    if s[i:i+3] == 'IOI': k += 1
    
print(j,k,sep='\n')
