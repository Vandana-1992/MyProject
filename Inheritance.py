class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_age(self):
        print("Age of", self.name, "is", self.age)
class Student(Person):
    def welcome(self):
        print("Welcome to Student class:")

name1 = input("Enter your name: ")
age1 = input("Enter your age: ")
p1_obj = Person(name1, age1)
p1_obj.print_age()
p2_obj = Student("Ravi", 35)
p2_obj.print_age()
p2_obj.welcome()


