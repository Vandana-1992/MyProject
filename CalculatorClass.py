class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            print("Can't divide by zero")
    def modulus(self):
        return self.num1 % self.num2


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
choice = int(input("Enter 1 for add, 2 for subtract, 3 for multiply, 4 for divide, 5 for modulus:"))
p1_obj = Calculator(number1, number2)
if choice == 1:
    res = p1_obj.add()
    print("Result is",res)
elif choice == 2:
    res = p1_obj.subtract()
    print("Result is",res)
elif choice == 3:
    res = p1_obj.multiply()
    print("Result is",res)
elif choice == 4:
    res = p1_obj.divide()
    print("Result is",res)
elif choice == 5:
    res = p1_obj.modulus()
    print("Result is",res)
else:
    print("Inavalid input")
