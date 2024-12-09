list1 = [8,6,8,4,6,4,9,7]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print("final:", list2)