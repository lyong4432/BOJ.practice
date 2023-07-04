n = int(input())
s1 = input()
s2 = input()

if n%2 == 0:
    if s1 == s2:
        print("Deletion succeeded")    
    else: print("Deletion failed")
else: 
    new = ''
    for i in s1:
        if i == "1":
            new += "0"
        else: new += "1"
    if new == s2:
        print("Deletion succeeded")    
    else: print("Deletion failed")
