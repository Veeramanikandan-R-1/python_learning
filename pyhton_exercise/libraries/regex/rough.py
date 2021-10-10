import re
word='mani is a no 1 good kani boy'
x=re.findall('boy\Z',word)
print(x)