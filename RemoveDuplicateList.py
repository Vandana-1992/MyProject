list1 = [2,4, 5, 6, 2, 6]
list2 = []
size = len(list1)
for i in range(0, size):
    for j in range(i+1, size - 1):
        if list1[i] == list1[j]:
            list1.pop(j)
print("new list:", list1)