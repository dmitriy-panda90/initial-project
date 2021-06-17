class Employee:
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year

    def show_employees_details(self):
        print("Name:",self.name,"Age:",self.age,"Year",self.year)


sara = Employee("Sara",18,1990)
sara.show_employees_details()