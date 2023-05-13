n = int(input())

for i in range(n):
    print('@'*3*n,' '*n,'@'*n,sep='')
for i in range(3*n):
    print('@'*n,' '*n,'@'*n,' '*n,'@'*n,sep ='')
for i in range(n):
    print('@'*n,' '*n,'@'*3*n,sep='')
