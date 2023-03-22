# 테스트 개수 t, 두 수를 더하는 코드 

t = int(input())
s_array = []
for i in range(0,t):
    a, b= map(int, input().split())
    s_array.append(a+b)

for i in range(0,t):
    print("Case #%d: %d" %(i+1, s_array[i]))
