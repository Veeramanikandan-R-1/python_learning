class employee:

    raise_amount=1.04 #class variables
    no_of_employees=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        employee.no_of_employees+=1 #incremented each time object is created

    @property #to continously access email as attribute with using parenthesis we use property above the method
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def full_name(self): #automatically takes instance attributes as self if we don't put error received
        return '{} {}'.format(self.first,self.last)

    @full_name.setter
    def full_name(self,name):
        first,last=name.split(" ")
        self.first=first
        self.last=last

    @full_name.deleter
    def full_name(self):
        print('delete name!')
        self.first=None
        self.last=None


emp1=employee('mani','kandan',25000)
emp2=employee('harish','kannan',30000)
emp1.full_name="me ana"
emp1.first='kalam'


print(emp1.first)
print(emp1.email) #anyone using our class need to change their code also so we use decorator above email method do we need to
print(emp1.full_name)

del emp1.full_name

