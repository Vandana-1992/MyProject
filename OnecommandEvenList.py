lst = []
even_lst = []
length = int(input("length of the list"))
for i in range(0,length):
    ele = int(input())
    lst.append(ele)
    print("list given is:", lst)
    print(lst[i] for i in range(0,length): if lst[i] % 2 == 0]