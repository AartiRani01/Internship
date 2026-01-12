# You are building a simple payroll system.

# Create a base class Employee with:
# attribute base_salary
# method calculate_salary() that returns base_salary
# Create two child classes inheriting from Employee:
# Developer
# additional attribute overtime_pay
# overrides calculate_salary() to return base_salary + overtime_pay
# Tester
# additional attribute bug_bonus
# overrides calculate_salary() to return base_salary + bug_bonus
# Create objects of both Developer and Tester and print their calculated salaries
class Employee:
    def __init__(self,base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary    

class Developer(Employee):
    def __init__(self,base_salary , overtime_pay):
        super().__init__(base_salary)
        self.overtime_pay = overtime_pay
    def calculate_salary(self):
        return super().calculate_salary() + self.overtime_pay    

class Tester(Employee):
    def __init__(self, base_salary, bug_bonus):
        super().__init__(base_salary)
        self.bug_bonus = bug_bonus
    def calculte_salary(self):
        return super().calculate_salary() + self.bug_bonus

dev = Developer(78000,5600)
tester = Tester(87698,8987)

print("Developer Salary is: ",  dev.calculate_salary())
print("Tester Salary is: ", tester.calculate_salary())