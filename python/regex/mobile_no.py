import re
mobile_no=str(input('enter a mobile number'))
mobile_pattern="^[9|8|7][0-9]{9}$"
check=re.findall(mobile_pattern,mobile_no)
if check:
	print("True")
else:
	print('False')
