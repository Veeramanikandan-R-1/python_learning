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

    def __repr__(self): #used for debugging and logging
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

    def __str__(self): # used for readable representation of objects
        return "{} - {}".format(self.full_name(),self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())

emp1=employee('veeramani','kandan',25000)
emp2=employee('harish','kannan',30000)

print(emp1.__repr__())
print(emp1.__str__())
print(repr(emp1))
print(str(emp1))

print(int.__add__(1,2))
print(emp1+emp2)

print(len('test'))
print('test'.__len__())
print(len(emp1))