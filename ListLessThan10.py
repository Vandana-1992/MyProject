# creating an empty list
lst = []
new_lst = []

# number of elements as input
n = int(input("Enter number of elements : "))
print("Enter the elements")
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)
print("list elements entered are: ")
print(lst)
for i in range(0, n):
    if(lst[i] < 10):
        new_lst.append(lst[i])
print("list of elements less than 10 are: ")
print(new_lst)
