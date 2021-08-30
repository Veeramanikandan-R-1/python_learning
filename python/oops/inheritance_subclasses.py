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

class developer(employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay) #we shall use the next line also don't use self inside super
        # employee.__init__(self,first,last,pay)
        self.prog_lang=prog_lang

class manager(employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print('already added')

    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.full_name())


dev1=developer('mani','kandan',25000,'python')
dev2=developer('harish','kannan',30000,'java')

mgr_1=manager('selva','kumar',40000,[dev1])


print(mgr_1.email)
mgr_1.add_emp(dev2)
print(mgr_1.print_emps())

# mgr_1.rem_emp(dev2)

print(mgr_1.print_emps())

# print(dev1.email)
# print(dev1.prog_lang)
# # print(help(developer)) #used to know class details
# print(dev1.pay)
# dev1.apply_increment()
# print(dev1.pay)

print(isinstance(mgr_1,manager)) #will return true
print(isinstance(mgr_1,employee))#will return true
print(isinstance(mgr_1,developer))#will return false

print(issubclass(manager,employee))#will return true
print(issubclass(developer,employee))#will return true
print(issubclass(manager,developer))#will return false