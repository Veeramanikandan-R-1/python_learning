import re
string='havE, a ,nice, day'
pattern='(?i)[a-z]+'
condition=re.findall(pattern,string)
print(condition)
