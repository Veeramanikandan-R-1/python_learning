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

print(employee.no_of_employees) # will return 0 since no object is created

emp1=employee('mani','kandan',25000)
emp2=employee('harish','kannan',30000)

emp1.raise_amount=1.05
#
# print(emp1.email)
# print(emp2.email)
# print(emp1.full_name()) #to call a method we need paranthesis if we fail it prints method not return values
# print(employee.full_name(emp1)) #printing using employee by passing obj as instance
# print(emp1.pay)
# emp1.apply_increment()
# print(emp1.pay)
#
# print(emp1.__dict__) #to view all attributes
# print(employee.__dict__) # raise amount will be stored here
#
# print(employee.raise_amount)
# print(emp1.raise_amount) #raise amount changed only to the particular employee
# print(emp2.raise_amount)

print(employee.no_of_employees)