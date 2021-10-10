class employee:

    raise_amount=1.04 #class variables
    no_of_employees=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+'@gmail.com'
        employee.no_of_employees+=1 #incremented each time object is created

    def full_name(self): #automatically takes instance attributes as self if we don't put error received
        return '{} {}'.format(self.first,self.last)

    def apply_increment(self):
        self.pay=int(self.pay * self.raise_amount)  #don't simply mention raise amount or use self.raise_amount
        # self.pay=int(self.pay*1.04)

    # creating classmethod using decorator
    @classmethod #alternative constructor
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount

    @classmethod #to create employee from string
    def from_string(cls,emp_str):
        first, last, pay = emp_str1.split('-')
        return cls(first,last,pay) #returns the employee object


emp1=employee('mani','kandan',25000)
emp2=employee('harish','kannan',30000)

# employee.set_raise_amount(1.05)
emp1.set_raise_amount(1.05) #will also change the raise amount for class

print(employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp_str1="mani-kandan-25000"
emp_str2="harish-kannan-30000"

new_emp1=employee.from_string(emp_str1)

print(new_emp1.email)
print(new_emp1.pay)
