class bank_account:    
    def create_account(acc_name,acc_type,acc_balance):
        user={}
        user["acc_name"]=str(input('enter username\n'))
        user["acc_type"]=str(input('enter a acc type\n'))
        user["acc_balance"]=int(input('enter a acc_balance'))
return user

class users(bank_account):
    def __init__(self,user1,user2):
        super().__init__(acc_number,acc_name,acc_balance)
        self.user1=user1
self.user2=user2
    def create_account(self):
self.user1=super().create_account()
self.user2=super().create_account()


    def deposit(self,amount_deposited):
acc_username=str(input('enter acc username'))
if self.user1["acc_name"]==acc_username:
	print("bal before deposit {}".format(self.user1["acc_balance"]))
	self.user1["acc_balance"]+=amount_deposited
	print("bal after deposit {}".format(self.user1["acc_balance"]))
else:			
	print("bal before deposit {}".format(self.user1["acc_balance"]))
	self.user2["acc_balance"]+=amount_deposited
	print("bal after deposit {}".format(self.user1["acc_balance"]))

    def withdrawal(self,amount_withdrawn):
       	acc_username=str(input('enter acc username'))
if self.user1["acc_name"]==acc_username:
	print("bal before withdrawal {}".format(self.user1["acc_balance"]))
	self.user1["acc_balance"]-=amount_withdrawn
	print("bal after withdrawal {}".format(self.user1["acc_balance"]))
else:	
	print("bal before withdrawal {}".format(self.user2["acc_balance"]))
	self.user2["acc_balance"]-=amount_withdrawn
	print("bal after withdrawal {}".format(self.user2["acc_balance"]))


    def display(self):
acc_username=str(input('enter acc username'))	
if self.user1["acc_name"]==acc_username:
	print("acc details\n acc_name:{}\nacc_type:{}\nacc_balance:{}".format(self.user1["acc_name"],self.user1["acc_type"],self.user1["acc_balance"]))
else:	
	print("acc details\n acc_name:{}\nacc_type:{}\nacc_balance:{}".format(self.user2["acc_name"],self.user2["acc_type"],self.user2["acc_balance"]))

    def transfer(self,amount):
from_acc=str(input('enter from user'))
to_acc=str(input('enter to user'))	
if self.user1["acc_name"]==acc_username:
		
def create_account(user):
    acc_name1=str(input('enter {}  acc name\n'.format(user)))
    acc_type1=input('enter {} account type savings or current\n'.format(user))
    acc_balance1=int(input('enter initial balance of the account for {}\n'.format(user)))
    user=bank_account(acc_name1,acc_type1,acc_balance1)

#create_account('user1')
#create_account('user2')


bank_user=user()
bank_user.create_account()

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
user=int(input('choose user by typing 1 or 2\n'))
if(user==1):
	user1.display()
else:
	user2.display()
#choice_fun()
elif(choice_1==4):
exit()
