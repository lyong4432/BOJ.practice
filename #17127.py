n = int(input())
nums = list(map(int, input().split()))
leng = n-3

def mul(x):
    hap = 1
    for i in x:
        hap *= i
    return hap

res = []
# 1
x = nums[:leng] 
p1 = mul(x) + sum(nums[leng:])
res.append(p1)

#2
nums1 =nums

for i in range(3):
    temp = nums1[0]
    nums1.pop(0)
    nums1.append(temp)  
    x = nums1[:leng] 
    p1 = mul(x) + sum(nums1[leng:])
    res.append(p1)
    
print(max(res))

# 진짜 어려웠는데 뿌듯함ㅎㅅㅎ
