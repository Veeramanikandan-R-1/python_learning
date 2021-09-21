import re

pan_nu=input('enter a pan no\n')

condition=re.findall("[A-Z]{5}[0-9]{4}[A-Z]{1}",pan_nu)
print(condition)
if condition:
	print('valid pan')
else:
	print('invalid pan')
