def check_sum(list1,target1):
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)-1):
            if list1[i] + list1[j] == target1:
                print("inside if loop")
                print(i,j)

lst = []
size_lst = int(input("enter the size of list:"))
print("enter the elements of list:")
ele = input()
lst.append(ele)
target = int(input("enter target number:"))
check_sum(lst,target)