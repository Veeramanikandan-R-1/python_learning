import re
roman_input=input("enter a roman numeral")
pattern_digit='(IX|IV|V?I{1,3}|V)'
pattern_tens='(X[CL]|L?X{0,3})'
pattern_hundreds='(C{MD}|D?C{0,3})'
pattern_thousands='M{0,3}'#since we need to find till 3000
condition=re.findall(pattern_thousands+pattern_hundreds+pattern_tens+pattern_digit,roman_input+'$')
print(condition)
if condition:
	print("True")
else:
	print("False")
