list1 = []
size1 = int(input("Enter the size of list:"))
print("enter the list items:")
for i in range(0, size1):
    ele = int(input())
    list1.append(ele)
print("content of list mentioned here:\n", list1)
great = list1[0]
for i in range(1, (size1-1)):
    if great < list1[i+1]:
        great = list1[i+1]
print("greatest number in list:", great)