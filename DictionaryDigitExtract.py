def add_dict(mydict):
    list1 = []
    for i in mydict:
        list1.append(mydict[i])
    output = sum(list1)
    return output
dict1 = {"ele1":4, "ele2": 6, "ele3": 9, "ele4": 10}
#sum1 = 0
#for i in dict1.values():
#    sum1 = sum1 + i
#print("total dictionary values:", sum1)
sum_dict = add_dict(dict1)
print("Sum of dictionary is:", sum_dict)
