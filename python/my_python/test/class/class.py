class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1
    def fullname(self):
        return '{0} {1}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#print emp_1.email
#print emp_2.email

#print Employee.fullname()
print emp_1.fullname()

emp_1.apply_raise()

print(Employee.raise_amount)
print (emp_1.raise_amount)
print (emp_2.raise_amount)

Employee.new_var = 'new'

print (emp_1.__dict__)
print (Employee.__dict__)

Employee.raise_amount = 1.05

print(Employee.raise_amount)
print (emp_1.raise_amount)
print(Employee.raise_amount)

emp_1.raise_amount = 1.02

print (emp_1.raise_amount)
print (emp_2.raise_amount)
print (emp_2.raise_amount)

print (Employee.num_of_emps)
