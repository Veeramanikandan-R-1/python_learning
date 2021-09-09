class employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+'@gmail.com'

    def full_name(self): #automatically takes instance attributes as self if we don't put error received
        return '{} {}'.format(self.first,self.last)

    def apply_increment(self):
        self.pay=int(self.pay*1.04)

emp1=employee('mani','kandan',25000)
emp2=employee('harish','kannan',30000)


print(emp1.email)
print(emp2.email)
print(emp1.full_name()) #to call a method we need paranthesis if we fail it prints method not return values
print(employee.full_name(emp1)) #printing using employee by passing obj as instance
print(emp1.pay)
emp1.apply_increment()
print(emp1.pay)