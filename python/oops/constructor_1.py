class employee:
    count=0
    def __init__(self,id,name): #constructor
        self.id=id #initializing class attributes
        self.name=name
        employee.count+=1

    def display(self):
        print('id:{} name:{}'.format(self.id,self.name))

emp1=employee(1,'mani')
emp1=employee(1,'mani')
emp1=employee(1,'mani')

print(employee.count) #should return 3 it will be incremented 3 times