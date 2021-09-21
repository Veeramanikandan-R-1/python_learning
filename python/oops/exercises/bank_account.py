class bank_account:
	def __init__(self,acc_number,acc_name,acc_balance):
		self.acc_number=acc_number
		self.acc_name=acc_name
		self.acc_balance=acc_balance

	def deposit(self,amount_deposited):
		print("bal before deposit {}".format(self.acc_balance))
		self.acc_balance+=amount_deposited
		print("bal after deposit {}".format(self.acc_balance))
	
	def withdrawal(self,amount_withdrawn):
		print("bal before withdrawal {}".format(self.acc_balance))
		self.acc_balance-=amount_withdrawn
		#print("bal after withdrawal {}".format(self.acc_balance))

	def bank_charges(self,amount_withdrawn):
		bank_charge=self.amount_withdrawn*0.05
		print('bank charge is {}'.format(bank_charge))
		self.acc_balance-=bank_charge	
		print("bal after withdrawal {}".format(self.acc_balance))

	def display(self):
		print("acc details\n acc_name:{}\nacc_number:{}\nacc_balance:{}".format(self.acc_name,self.acc_number,self.acc_balance))

#acc1=bank_account(122,'mani',1000)
#acc1.deposit(1000)
#acc1.withdrawal(1000)
acc_name1=str(input('enter acc holder name\n'))
acc_number1=int(input('enter a account number\n'))
acc_balance1=int(input('enter initial balance of the account\n'))
acc1=bank_account(acc_name1,acc_number1,acc_balance1)
def choice_fun():
	choice=int(input("enter you choice:\n1 for deposit\n2 for withdrawal\n3 for viewing account details\n4 for exit\n"))
	return choice
choice_1=choice_fun()
#print(choice_1)
if(choice_1==1):
	deposit_amount=int(input('enter amount to be deposited'))
	acc1.deposit(deposit_amount)
	#choice_fun()
elif(choice_1==2):
	withdrawal_amount=int(input('enter amount to be withdrawn'))
	acc1.withdrawal(withdrawal_amount)
	#choice_fun()
	acc1.bank_charge()
elif(choice_1==3):
	acc1.display()
	#choice_fun()
elif(choice_1==4):
	exit()
