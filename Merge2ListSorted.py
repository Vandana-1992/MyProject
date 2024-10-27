list1 = []
list2 = []
length1 = int(input("enter the size of 1st list:"))
length2 = int(input("enter the size of 2nd list:"))
print("enter the first list:")
for i in range(0, length1):
    ele1 = int(input())
    list1.append(ele1)
print("enter the second list:")
for j in range(0, length2):
     ele2 = int(input())
     list2.append(ele2)
#sort 1st list
list1 = list1.sort()
list2 = list2.sort()
print("After sorting the 2 lists:")
print(list1)
print(list2)
for i in range(0, max(length1, length2)):
    for j in range(i, length2):
        if list1[i] < list2[j]:
            tmp = list1[i]
            list1[i] = list2[j]
            list2[j] = tmp
list2 = sorted(list2)
for x in range(len(list1 + list2)):
    print(list1[x] + list2[x])



