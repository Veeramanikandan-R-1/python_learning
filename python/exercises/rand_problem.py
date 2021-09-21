'''
A low-level implementation of the classic game “Mastermind”. We need to write a program that generates a four-digit random code and the user needs to guess the code in 10 tries or less. If any digit out of the guessed four-digit code is wrong, the computer should print out “B”. If the digit is correct but at the wrong place, the computer should print “Y”. If both the digit and position is correct, the computer should print “R”. Example:

mastermind-python
'''
import random
number_a=[x for x in str(random.randint(9999,1000))]
print(number_a)
def check_fun(input_no):
	condition=True
	string_result=""
	for i in range(len(inp_number)):
		if(inp_number[i]==number_a[i]):
			string_result+="R"
		elif(inp_number[i] in number_a):
			string_result+="Y"
			condition=False	
		elif(inp_number[i] not in number_a):
			string_result+="B"
			condition=False
	return condition,string_result
i=0
while(i<10):
	inp_number=[x for x in str(input('enter a four digit number\n'))]
	while inp_number:
		if(len(inp_number)==4):
			break
		else:
			print("invalid number")
			inp_number=[x for x in str(input('enter a four digit number\n'))]
	if (len(inp_number)==4):
		checking_var=check_fun(inp_number)
		#print(checking_var[0])
		if(checking_var[0]):
			print('you guessed it {}'.format(inp_number))
			break
		else:
			print(checking_var[1])
	i+=1
else:
	print("chances over,no more try!")
