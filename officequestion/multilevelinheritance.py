# You are building an employee management system.

# Create a class Employee with:
# attribute salary
# method get_salary() that returns salary
# Create a class Manager that inherits from Employee and:
# adds attribute bonus
# overrides get_salary() to return salary + bonus
# Create a class SeniorManager that inherits from Manager and:
# adds attribute stock_options
# overrides get_salary() using super() to include stock option


class Employee:
    def __init__(self,salary):
        self.salary = salary

    def get_salary(self):
        return self.salary
    
class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus
    def get_salary(self):
        return self.salary + self.bonus    

class SeniorManager(Manager):
    def __init__(self, salary, bonus, stock_option):
        super().__init__(salary,bonus)
        self.stock_option = stock_option
    def get_salary(self,pf):
        return super().get_salary() + self.stock_option+pf    # with parenthesis this calling as integer (integer is calling without a parenthesis)
        # self.stock_option = stock_option
       

sm = SeniorManager(67000,8000,1000)
print("The SeniorManager salary is: ",sm.get_salary(1000))