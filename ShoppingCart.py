class Cart:
    def __init__(self):
        self.items = []
        self.price = []
    def cart_add(self, veg1, rate1):
        self.items.append(veg1)
        self.price.append(rate1)
    def cart_remove(self, veg1, rate1):
        self.items.remove(veg1)
        self.price.remove(rate1)
    def cart_display(self):
        for x in range(0, len(self.items)):
            print("items in the cart",self.items[x],"its price is ",self.price[x])
    def total_amount(self):
        total = 0
        for j in range(0,len(self.items)):
            total = total + self.price[j]
            return total


p1_obj = Cart()
number_items = int(input("Enter number of items: "))
for i in range(number_items):
    veg = input("enter the vegetable to be added:")
    rate = float(input("enter the rate of the veg:"))
    p1_obj.cart_add(veg, rate)
choice = int(input("Do you want to remove any items from cart? 1 if yes, 2 if no:"))
if choice == 1:
    veg = input(print("enter the item name:"))
    rate = float(input("enter the rate of that item:"))
    p1_obj.cart_remove(veg, rate)
elif choice == 2:
    p1_obj.cart_display()
    res = p1_obj.total_amount()
    print("total price of items:", res)
else:
    print("invalid choice")