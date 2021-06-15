class Employee:

 def __init__(self, name, salary, attendance):
        self.name = name
        self.salary = salary
        self.attendance = attendance

 def attendance_check(self):
        print(""+self.name + " " +self.salary+" " + str(self.attendance))

 def show_employees_details(self):
     print(" " + self.name + " " + self.salary)

sara = Employee ("sara", "1325", False)
sara.attendance_check()
sara.show_employees_details()

michel = Employee ("Michel", "1250", True)
michel.show_employees_details()
michel.attendance_check()