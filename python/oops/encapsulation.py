class computer:
    def __init__(self):
        self.__max_price=900

    def sell(self):
        print('selling price is {}'.format(self.__max_price))

    def setMaxPrice(self,price):
        self.__max_price=price

c=computer()
c.sell()

c.__max_price=1000
c.sell()

c.setMaxPrice(1000) #change using setter function possible
c.sell()

