class vehicle:
    color="white"
    def __init__(self,name,max_speed,mileage,capacity_1):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        self.capacity_1=capacity_1
		
    def capacity(self):
        print('capacity of {} is {} passengers'.format(self.name,self.capacity_1))
    def fare(self):
        print("fare is {}".format((self.capacity_1)*100))
	
		
class bus(vehicle):
	def capacity(self,capacity_1=100):
		return super().capacity()
	def fare(self):
		total_fare=(self.capacity_1*100)+(0.1*self.capacity_1)
		print("fare is {}".format(total_fare))	
		


vehicle1=vehicle("abc",200,60,50)
vehicle1.capacity()
vehicle1.fare()
bus1=bus("bcd",300,50,50)
print(bus1.mileage)
bus1.capacity()
print(bus1.color)
bus1.fare()
print(type(bus1)) #prints bus belongs to which class
print(isinstance(bus1,vehicle))
