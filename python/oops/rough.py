class employee:
    def __init__(self,name,id,age):
        self.name=name
        self.age=age
        self.id=id

emp1=employee('mani',1,23)

print(getattr(emp1,'age'))

setattr(emp1,'age',25)

print(getattr(emp1,'age'))


# emp1=employee(1,'mani') we should not pass values from here

