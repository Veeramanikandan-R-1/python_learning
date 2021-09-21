import re
card_number=str(input('enter credit card number\n'))
pattern='^[4|5|6][0-9]{3}-{0,1}[0-9]{4}-{0,1}[0-9]{4}-{0,1}[0-9]{4}$'
condition=re.findall(pattern,card_number)
if(condition):
	print("true")
else:
	print("false")

