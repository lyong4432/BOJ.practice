list_all = []
list_max = []
list_max_index = []

for i in range(9):
    a = list(map(int, input().split()))
    list_all.append(a)


for i in list_all:
    list_max.append(max(i))
    list_max_index.append(i.index(max(i)))

max_index = list_max.index(max(list_max))

print(max(list_max))
print(max_index+1,list_max_index[max_index]+1)
