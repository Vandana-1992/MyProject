list1 = []
new_list1 = []
j = 0
size_arr = int(input("Enter the size of the array:"))
print("enter the array elements:")
for i in range(size_arr):
    ele = int(input())
    list1.append(ele)
print("list elements are:", list1)
position = int(input("enter the index from where you want to split:"))
new_list1 = list1[:position]
print(list1[position:]+ new_list1[::])