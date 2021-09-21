import re
string=input('enter a string\n')
condition=r'[aeiouAeiou][aeiouAEIOU]+'
x=re.findall(condition,string)
print(x)
