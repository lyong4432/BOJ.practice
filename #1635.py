n = int(input())
postFix = list(input())
nums = []

for i in range(n):
    nums.append(input())
dic = {}
j = 0
for i in postFix:
    if i.isalpha() and i not in dic:
        dic[i] = nums[j]
        j += 1

stack = []
a, b = 0, 0

for i in postFix:
    if i.isalpha():
        stack.append(int(dic[i]))
    elif i == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a+b)
    elif i == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a-b)
    elif i == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a*b)
    elif i == '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a/b)

print("{:.2f}".format(stack.pop()))
