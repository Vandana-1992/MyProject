def checkfun(list1, list2,list3):
    len1 = int(len(list1))
    len2 = int(len(list2))
    if len1 > len2:
        for i in range(0, len1):
            if list1[i] == list2[i]:
                lst3.append(list1[i])
                break
    if len2 > len1:
        for i in range(0, len2):
            if list2[i] == list2[i]:
                lst3.append(list2[i])
                break
    print("List of common elements in lists are below")
    print(lst3)

lst1 = []
lst2 = []
lst3 = []
size1 = int(input("Enter the size of 1st list:"))
size2 = int(input("Enter the size of 2ns list:"))
print("Enter the elements of 1st list:")
for x in range(0, size1):
    ele1 = input()
    lst1.append(ele1)
    print("Enter the elements of 2nd list:")
    for y in range(0, size2):
        ele2 = input()
        lst2.append(ele2)
        print("Elements of 1st and 2nd list are below")
        print(lst1)
        print(lst2)
        checkfun(lst1, lst2,lst3)