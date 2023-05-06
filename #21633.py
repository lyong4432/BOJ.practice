k = int(input())
hap = (25)+k*0.01
if hap<=100:
    print(f'{100:.2f}')
elif hap>=2000:
    print(f'{2000:.2f}')
else: 
    print(f'{hap:.2f}')
