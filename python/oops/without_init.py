class employee:
    id=1
    name='mani'

    def display(self): #without init it constructor initializes object alone   
        print('id:{} name:{}'.format(self.id,self.name)) #don't use self.id

emp1=employee()
# emp1=employee(1,'mani') we should not pass values from here

# print(employee.count) #should return 3 it will be incremented 3 times
emp1.display()