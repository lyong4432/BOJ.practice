
i = 1

while True:
    a = input().strip()
    b = input().strip()
    if a == b == 'END':
        break

    a = list(a)
    a.sort()
    b = list(b)
    b.sort()
    
    if a ==b: print(f"Case {i}: same")
    else: print(f"Case {i}: different")
    
    i+=1
