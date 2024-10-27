class Person:
    def __init__(self, name, country, year_of_birth):
        self.name = name
        self.country = country
        self.year_of_birth = year_of_birth
    def determineage(self):
        age = int(2024 - self.year_of_birth)
        return age

name1 = input("Enter the name:")
country1 = input("enter the country:")
birthyear = int(input("Enter the year of birth:"))
p1_obj = Person(name1, country1, birthyear)
age_person = p1_obj.determineage()
print("age of", name1, "is:", age_person)