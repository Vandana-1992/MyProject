list1 = []
list_extra = []
k = 0
size1 = int(input("Enter the size of the array: "))
print("Enter the elements of the array: ")
for i in range(size1):
    ele = input()
    list1.append(ele)
    print("elements of array:", list1)
for x in range(0, size1):
    for y in range((x+1), size1):
        if list1[x] == list1[y]:
            for k in range(y, size1):
                list_extra[k] = list_extra[k+1]
        y = y - 1
        size1 = size1 - 1
print("after removing duplicates:")
print(list_extra)