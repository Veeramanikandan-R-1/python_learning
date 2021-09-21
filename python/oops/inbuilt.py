class employee:
    def __init__(self,name,id,age):
        self.name=name
        self.age=age
        self.id=id

emp1=employee('mani',1,23)

print(emp1.__doc__)
print(emp1.__dict__)
#print(emp1.__name__)
# print(emp1.__module__)
#print(emp1.__bases__)
