class Stack:
    def __init__(self):
        self.item = []
    def push(self, num1):
        self.item.append(num1)
    def pop(self, num1):
        self.item.pop(num1)
    def print_stack(self):
        for i in range(0, len(self.item)):
            print(self.item[i])

num = int(input("enter the item:"))
operation = input("enter 1 for push, 2 for pop:")
p1_obj = Stack()
if operation == "1":
    p1_obj.push(num)
    p1_obj.print_stack()
    choice = input("Do you want to add again? if yes-y no-n:")
    if choice == "y":
        new_num = int(input("enter the item to add:"))
        p1_obj.push(new_num)
        p1_obj.print_stack()
    elif choice == "n":
        exit()
if operation == "2":
    print("items in the stack", p1_obj.print_stack())
    num_remove = int(input("enter the item to remove:"))
    p1_obj.pop(num_remove)
    p1_obj.print_stack()
    choice = input("Do you want to remove? if yes-y no-n:")
    if choice == "y":
        p1_obj.pop(num_remove)
        p1_obj.print_stack()
    elif choice == "n":
        exit()