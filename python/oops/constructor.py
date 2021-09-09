class employee:
    def __init__(self,id,name): #constructor
        self.id=id #initializing class attributes
        self.name=name

    def display(self):
        print('id:{} name:{}'.format(self.id,self.name))

emp1=employee(1,'mani')
emp1.display()