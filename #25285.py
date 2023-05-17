t = int(input())
res = []
for i in range(t):
    cm, kg = map(int,input().split())
    bmi = kg/((cm/100)**2)
    if cm >= 204:
        res.append(4)
    elif cm >= 161:
        if  25.0 > bmi >= 20.0:
            res.append(1)
        elif (20.0> bmi >= 18.5) or (30.0>bmi>=25.0):
            res.append(2)
        elif (18.5>bmi>=16.0) or (35.0>bmi>=30.0):
            res.append(3)
        elif (bmi <16.0 or bmi>=35.0):
            res.append(4)
    elif cm >= 159:
        if 35.0>bmi>=16.0:
            res.append(3)
        elif bmi >= 35.0 or bmi <16.0:
            res.append(4)
    elif cm >= 146:
        res.append(4)
    elif cm >=140.1:
        res.append(5)
    else: res.append(6)

for i in res:
    print(i)
