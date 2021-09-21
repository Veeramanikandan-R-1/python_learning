class bank:
	minimum_bal=1000
	def __init__(self,acc_name,acc_type,initial_bal):
		self.acc_name=acc_name
		self.acc_type=acc_type
		self.initial_bal=initial_bal

	def deposit(self,amount_deposited):
		self.initial_bal+=amount_deposited

	def withdrawal(self,amount_withdrawn):
		if((self.initial_bal-amount_withdrawn)>bank.minimum_bal):
			self.initial_bal-=amount_withdrawn
		else:
			print("sorry minimum bal {} should be maintained your balance is {}".format(bank.minimum_bal,self.initial_bal))
	def display(self):
		print("acc details\n acc_name:{}\nacc_type:{}\nacc_balance:{}".format(self.acc_name,self.acc_type,self.initial_bal))

#	def transfer(self,to_acc,amount):
#		to_acc.initial_bal+=amount
#		self.initial_bal-=amount
	@staticmethod 
	def transfer(from_acc,to_acc,amount):
		to_acc.initial_bal+=amount
		from_acc.initial_bal-=amount

	@classmethod
	def set_min_bal(cls,amount_min):
		cls.minimum_bal=amount_min
class history(bank):
	history_list=[]
	def __init__(self,acc_name,acc_type,initial_bal):
		super().__init__(acc_name,acc_type,initial_bal)
	def deposit(self,amount_deposited):
		super().deposit(amount_deposited)
		history.history_list.append("{} depostied {}".format(self.acc_name,amount_deposited))
	def withdrawal(self,amount_withdrawn):
		super().withdrawal(amount_withdrawn)
		history.history_list.append("{} withdrawn {}".format(self.acc_name,amount_withdrawn))
	def transfer(from_acc,to_acc,amount):
		bank.transfer(from_acc,to_acc,amount)
		history.history_list.append("{} transferred {} to {}".format(from_acc.acc_name,amount,to_acc.acc_name))
	def show_transaction_history():
		print(history.history_list)

#acc1=bank("mani","savings",1000) 
acc1=history("mani","savings",2000)
acc2=history("harish","current",500)

acc1.deposit(100)
acc2.deposit(100)
acc1.display()
acc2.display()
bank.set_min_bal(2000) #using setter fun
acc1.withdrawal(200)
acc2.withdrawal(200)
acc1.display()
acc2.display()
history.transfer(acc1,acc2,200)
acc1.display()
acc2.display()
history.show_transaction_history()
