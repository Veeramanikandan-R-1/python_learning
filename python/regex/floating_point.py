'''
You are given a string .
Your task is to verify that  is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

 Number can start with +, - or . symbol.
For example:
✔
+4.50
✔
-1.0
✔
.5
✔
-.7
✔
+.4
✖
 -+4.5

 Number must contain at least  decimal value.
For example:
✖
 12.
✔
12.0  

 Number must have exactly one . symbol.
 Number must not give any exceptions when converted using .
'''
import re
number=input("enter a number\n")
#condition=re.findall(r'^[+-]?[0-9]*.[0-9]+$',number)
condition=re.findall(r'^[+-]?[0-9]*.[0-9]+',number)
print(condition)
if condition:
	print('True')
else:
	print('False')
