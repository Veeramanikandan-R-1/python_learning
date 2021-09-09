class employee:
    count=0
    def __init__(self):
        print('non parameterized constructor')

    def display(self,id,name):
        print('id:{} name:{}'.format(id,name)) #don't use self.id

emp1=employee()
# emp1=employee(1,'mani') we should not pass values from here

# print(employee.count) #should return 3 it will be incremented 3 times
emp1.display('1','mani')