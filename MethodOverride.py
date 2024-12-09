class Employee1:
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal
    def display_name(self):
        print(self.name)
    def display_sal(self):
        print("salary is", self.sal)

class Employee2(Employee1):
    def __init__(self, name, sal, incv):
        super().__init__(name, sal)
        self.incv = incv
    def display_sal(self):
        print("Employee2 salary:", self.incv + self.sal)

p1_obj = Employee1("Vandana", 10000)
p2_obj = Employee2("Rajesh", 20000, 5000)
p1_obj.display_name()
p1_obj.display_sal()
p2_obj.display_name()
p2_obj.display_sal()
